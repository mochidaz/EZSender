class ParseConfig(object):
    def __init__(self, config):
        self.config = config

    def parse_config(self):
        with open(self.config, 'r') as f:
            file = f.readlines() # Reading the lines in the file one by one
            lines = (line.rstrip() for line in file)
            lines = list(line for line in lines if line and not line.startswith('#')) # Non-blank lines in a list
            lines = [i.split('=') for i in lines]
            var = [variable[0].strip() for variable in lines]
            val =  [int(value[1]) if value[1].strip().isdigit() else value[1] for value in lines]
            res = dict(zip(var, val))

        return res

    def get_mailist(self):
        return self.parse_config().get('mailist')
    
    def get_subject(self):
        return self.parse_config().get('subject')

    def get_name(self):
        return self.parse_config().get('from_name')

    def get_email(self):
        return self.parse_config().get('from_email')

    def get_letter(self):
        return self.parse_config().get('letter')

    def get_random_link(self):
        return self.parse_config().get('random_link')

    def get_delay(self):
        return self.parse_config().get('setDelay')

    def get_smtp_host(self):
        return self.parse_config().get('smtpHost')

    def get_smtp_port(self):
        return self.parse_config().get('smtpPort')

    def get_smtp_user(self):
        return self.parse_config().get('smtpUser')

    def get_smtp_pass(self):
        return self.parse_config().get('smtpPass')
