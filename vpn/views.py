from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sys, ast

from vpn.models import Datacenter, firewall

def index(request):
    firewall_list = []
    datacenter_list = []
    firewall_status = []
    # This will grab each datacenter object (if they're marked active) from the 
    # database and add them to a list
    for each in Datacenter.objects.order_by('datacenter_code'):
        if each.datacenter_active == True: datacenter_list.append(each)
    # Same thing here - grab our firewalls and append to a list
    for each in firewall.objects.order_by('firewall_name'):
        if each.firewall_active == True: firewall_list.append(each)
    # Now we pass those lists to the buildrows function to assemble our HTML table
    firewall_status = buildrows(firewall_list, datacenter_list)
    # We're also going to apply a template to make the page look fancy
    template = loader.get_template('web/index.html')
    # This is taking all of our lists, and passing them into our HTML template
    # so that it can build the page semi-automatically
    context = {
        'datacenter_list':datacenter_list,
        'firewall_list': firewall_list,
        'firewall_status':firewall_status,
    }
    return HttpResponse(template.render(context,request))

def buildrows(firewall_list, datacenter_list):
    firewallstatus = []
    # We will iterate through each firewall and compile each row for our table
    for fw in firewall_list:
        # The first cell in our row is going to be the firewall name and it's own VPN peer IP
        onerow = "<td><b>%s</b><i>%s</i></td>" % (fw.firewall_name, fw.firewall_vpnip)
        # Now we iterate through every datacenter, in order to see which ones we have a
        # connection to from this firewall
        for dc in datacenter_list:
            # First thing is first - If this firewall contains the name of the datacenter
            # then we'll print N/A, since we wouldn't expect a VPN to itself 
            if str(dc.datacenter_code) in str(fw.firewall_name):
                onerow += ("<td>N/A</td>")
                continue
            # Also, if there is no VPN status in the database, then just print 'No Status'
            if not fw.firewall_vpnstatus:
                onerow += ("<td>No Status</td>")
                continue
     
            # This portion is pretty self-explanatory - We parse the vpnstatus field in the
            # database. If the state of the connection is 'VPNUP', then we print a cell for
            # that datacenter with the text 'UP'. If the state is 'VPNDOWN', then we print
            # 'DOWN'. And if nothing matches, print 'No Status'
            statuslist = ast.literal_eval(fw.firewall_vpnstatus)
            try:
                status = statuslist[dc.datacenter_code]
                if status == "VPNUP":
                    onerow += ("<td class=\"vpnup\">")
                    onerow += ("UP")
                elif status == "VPNDOWN":
                    onerow += ("<td class=\"vpndown\">")
                    onerow += ("DOWN")
                else:
                    onerow += ("<td>")
                    onerow += ("No Status")
                    onerow += ("</td>")
            except KeyError:
                onerow += ("<td>")
                onerow += ("No Status")
                onerow += ("</td>")
        # Once complete, we append this row to the status list
        firewallstatus.append(onerow)
    
    # All done! Return our list of statuses!
    return firewallstatus