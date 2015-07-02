from netmiko.ssh_connection import SSHConnection

class Alcatel7210SSH(SSHConnection):

    def enable(self):
        '''
        No enable mode on Alcatel 7210
        '''
        pass


    def exit_enable_mode(self, exit_command=''):
        '''
        No enable mode on Alcatel 7210
        '''
        pass
