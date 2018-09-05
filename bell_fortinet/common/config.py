# Copyright 2015 Fortinet Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from fortiosclient import client
from oslo_config import cfg

from bell_fortinet._i18n import _

import configparser

ini_file_path = "/etc/neutron/plugins/ml2/ml2_conf.ini"
config = configparser.ConfigParser()
config.read(ini_file_path)

ml2_fortinet = config["ml2_fortinet"]

ML2_FORTINET = [
    cfg.StrOpt('address', default=ml2_fortinet["address"],
               help=_('The address of fortigates to connect to')),
    cfg.StrOpt('port', default=ml2_fortinet["port"],
               help=_('The FGT port to serve API requests')),
    cfg.StrOpt('protocol', default=ml2_fortinet["protocol"],
               help=_('The FGT uses which protocol: http or https')),
    cfg.StrOpt('username', default=ml2_fortinet["username"],
               help=_('The username used to login')),
    cfg.StrOpt('password', default=ml2_fortinet["password"], secret=True,
               help=_('The password used to login')),
    cfg.StrOpt('int_interface', default=ml2_fortinet["int_interface"],
               help=_('The interface to serve tenant network')),
    cfg.StrOpt('ext_interface', default=ml2_fortinet["ext_interface"],
               help=_('The interface to the external network')),
    cfg.StrOpt('tenant_network_type', default=ml2_fortinet["tenant_network_type"],
               help=_('tenant network type, default is vlan')),
    cfg.StrOpt('vlink_vlan_id_range', default=ml2_fortinet["vlink_vlan_id_range"],
               help=_('vdom link vlan interface, default is 3500:4000')),
    cfg.StrOpt('vlink_ip_range', default=ml2_fortinet["vlink_ip_range"],
               help=_('vdom link interface IP range, '
                      'default is 169.254.0.0/20')),
    cfg.StrOpt('vip_mappedip_range', default=ml2_fortinet["vip_mappedip_range"],
               help=_('The intermediate IP range in floating IP process, '
                      'default is 169.254.128.0/23')),
    cfg.BoolOpt('npu_available', default=ml2_fortinet["npu_available"],
                help=_('If npu_available is True, it requires hardware FGT'
                       'with NPU, default is True')),
    cfg.BoolOpt('enable_default_fwrule', default=False,
                help=_('If True, fwaas will add a deny all rule automatically,'
                       ' otherwise users need to add it manaully.')),
    cfg.StrOpt('av_profile', default=None,
               help=_('Assign a default antivirus profile in FWaaS, '
                      'the profile must exist in FGT, default is ""')),
    cfg.StrOpt('webfilter_profile', default=None,
               help=_('Assign a default web filter profile in FWaaS, '
                      'the profile must exist in FGT, default is ""')),
    cfg.StrOpt('ips_sensor', default=None,
               help=_('Assign a default IPS profile in FWaaS, '
                      'the profile must exist in FGT, default is ""')),
    cfg.StrOpt('application_list', default=None,
               help=_('Assign a default application control profile in FWaaS,'
                      ' the profile must exist in FGT, default is ""')),
    cfg.StrOpt('ssl_ssh_profile', default=None,
               help=_('Assign a default SSL/SSH inspection profile in FWaaS, '
                      'the profile must exist in FGT, default is ""'))
]

cfg.CONF.register_opts(ML2_FORTINET, "ml2_fortinet")


ml2 = config["ml2"]

ML2 = [
    cfg.StrOpt('type_drivers', default=ml2["type_drivers"],
               help=_('The address of fortigates to connect to')),
    cfg.StrOpt('tenant_network_types', default=ml2["tenant_network_types"],
               help=_('The address of fortigates to connect to')),
    cfg.StrOpt('extension_drivers', default=ml2["extension_drivers"],
               help=_('The address of fortigates to connect to')),
    cfg.StrOpt('mechanism_drivers', default=ml2["mechanism_drivers"],
               help=_('The address of fortigates to connect to')),
]

cfg.CONF.register_opts(ML2, "ml2")

fgt_info = {
    'address': ml2_fortinet["address"],
    'port': ml2_fortinet["port"],
    'protocol': ml2_fortinet["protocol"],
    'username': ml2_fortinet["username"],
    'password': ml2_fortinet["password"],
    'int_interface': ml2_fortinet["int_interface"],
    'ext_interface': ml2_fortinet["ext_interface"],
    'tenant_network_type': ml2_fortinet["tenant_network_type"],
    'vlink_vlan_id_range': ml2_fortinet["vlink_vlan_id_range"],
    'vlink_ip_range': ml2_fortinet["vlink_ip_range"],
    'vip_mappedip_range': ml2_fortinet["vip_mappedip_range"],
    'npu_available': ml2_fortinet["npu_available"],
    'enable_default_fwrule': False,
    'av_profile': None,
    'webfilter_profile': None,
    'ips_sensor': None,
    'application_list': None,
    'ssl_ssh_profile': None
}


def get_apiclient():
    """Fortinet api client initialization."""
    api_server = [(fgt_info['address'], fgt_info['port'],
                   'https' == fgt_info['protocol'])]
    return client.FortiosApiClient(
        api_server, fgt_info['username'], fgt_info['password'])
