#
# Project Kimchi
#
# Copyright IBM, Corp. 2013
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext

from kimchi.i18n import messages as kmessages

_ = gettext.gettext


messages = {
    "GINNET0001E": _("Failed to read /etc/resolv.conf because %(reason)s"),
    "GINNET0002E": _("Failed to write /etc/resolv.conf because %(reason)s"),
    "GINNET0003E": _("Invalid network parameters. Details: %(err)s"),
    "GINNET0004E": _("Unable to update interface configuration. "
                     "Details: %(err)s"),
    "GINNET0005E": _("Invalid parameter for DNS servers"),
    "GINNET0006E": _("Invalid parameter for interface ip address"),
    "GINNET0007E": _("Invalid parameter for interface netmask"),
    "GINNET0008E": _("Invalid parameter for network gateway"),

    "GINUSER0001E": _("Specify name, password, group and profile for the new "
                      "user."),
    "GINUSER0002E": _("User name is a required string."),
    "GINUSER0003E": _("User password is a required string."),
    "GINUSER0004E": _("User group is a required string."),
    "GINUSER0005E": _("User profile is required and should be one among "
                      "kimchiuser, virtuser or admin."),
    "GINUSER0006E": _("Could not add user '%(user)s' to kvm group."),
    "GINUSER0007E": _("Could not add user '%(user)s' to sudoers list."),
    "GINUSER0008E": _("The user name '%(user)s' is already in use'."),
    "GINUSER0009E": _("Could not create user '%(user)s'."),
    "GINUSER0010E": _("Could not delete user '%(user)s'."),
    "GINUSER0011E": _("User '%(user)s' does not exist."),
    "GINUSER0012E": _("Could not delete group '%(group)s'"),
    "GINUSER0013E": _("Group for user '%(user)s' does not exist for removal.")
}
messages.update(kmessages)
