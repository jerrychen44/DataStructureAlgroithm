'''
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.
'''

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def printout_all(self):
        print('+++++++++++++ debug print +++++++++++++')
        print('self.name:',self.name)
        print('groups')
        glist = '    '
        for g in self.groups:
            glist += g.name +', '
        print(glist)


        print('users')
        ulist = '    '
        for u in self.users:
            ulist += u +', '
        print(ulist)
        print('------------ debug print ------------')


def debug_print():
    parent.printout_all()
    child.printout_all()
    child2.printout_all()
    sub_child.printout_all()
    sub_child2.printout_all()
    sub_child3.printout_all()

#Group
parent = Group("parent_group")
child = Group("child_group")
child2 = Group("child2_group")
sub_child = Group("subchild_group")
sub_child2 = Group("subchild2_group")
sub_child3 = Group("subchild3_group")

#add user
sub_child.add_user("X_user")
sub_child.add_user("Y_user")

sub_child3.add_user("Y3_user")

child.add_user("A_user")
child.add_user("B_user")
child2.add_user("A2_user")
child2.add_user("B2_user")


parent.add_user("1_user")
parent.add_user("2_user")

#set group
child.add_group(sub_child)
child2.add_group(sub_child2)
child2.add_group(sub_child3)


parent.add_group(child)
parent.add_group(child2)

#debug
#debug_print()

'''
Write a function that provides an efficient look up of whether the user is in a group.
'''



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if len(user) == 0 or group == None:
        return False
    #debug_print()
    return helper(user, group)


def helper(user, group):

    #print('cur group in',group.name)

    if len(group.groups) == 0 and len(group.users) == 0:
        #print('End of groups')
        return

    #finding the user
    if user in group.users:
        print('find usr',user,'in ',group.name)
        return True

    #we might have muti-group inside a group
    for g in group.groups:
        rst= helper(user, g)
        if rst == True:
            return rst

    return False


print('test case1')
userid = 'Y3_user'
findgroup=parent
print(is_user_in_group(userid,findgroup))
'''
output:
find usr Y3_user in  subchild3_group
True
'''
print('test case2')
userid = '2_user'
findgroup=child2
print(is_user_in_group(userid,findgroup))
'''
False
'''

print('test case3')
userid = ''
findgroup=sub_child3
print(is_user_in_group(userid,findgroup))
'''
False
'''

print('test case4')
userid = '2_user'
findgroup=None
print(is_user_in_group(userid,findgroup))
'''
False
'''
##
