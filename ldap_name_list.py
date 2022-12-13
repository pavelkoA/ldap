import os
import sys
from ldap3 import Server, Connection, SAFE_SYNC, SUBTREE

current_user = os.getlogin()

my_server = '192.168.0.13'
user_admin = 'strike\\server'
password_user_server = '@vt0pr0m'
AD_SEARCH_TREE = 'dc=strike,dc=local'
ad_filter_member = '(&(ObjectClass=GroupOfUniqueNames)(uniquemember=uid=Артем Павелко,dc=strike,dc=local))'

def ldap_connnection():
    server = my_server
    return Connection(server, user=user_admin, password=password_user_server, auto_bind=True)

with ldap_connnection() as c:
    c.search(AD_SEARCH_TREE, '(&(objectCategory=Person)(sAMAccountName=' + current_user + '))', search_scope=SUBTREE, attributes=['distinguishedName'])
    full_name_user = c.entries[0].distinguishedName


with ldap_connnection() as c:
    c.search(AD_SEARCH_TREE, '(&(objectCategory=Group))', search_scope=SUBTREE, attributes=['member', 'cn'])
    members_list = c.entries

my_member_list = []
for m in members_list:
    for item_member in m.member:
        if item_member in full_name_user:
            my_member_list.append(str(m.cn))

with open('base.txt', 'r') as file_1c_open:
    file_read = file_1c_open.read()
    print(file_read)



