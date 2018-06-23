from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None,
                 mail1=None, mail2=None, mail3=None, homepage=None, address2=None, home2=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.homepage = homepage
        self.address2 = address2
        self.home2 = home2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:" % (self.id, self.first_name,)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




