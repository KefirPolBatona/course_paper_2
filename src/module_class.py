class Output:
    """
    Класс Output принимает сведения об операции в виде аргументов: id, state, date, operationAmount, description, from_,
    to.

    Преобразует формат даты.

    Определяет аргументы: amount (сумма), currency_name (валюта), from_name (платёжная система отправителя),
    from_number_hidden (скрытый счет отправителя), to_name (платёжная система получателя),
    to_number_hidden (скрытый счет отправителя).

    Возвращает экземпляр класса с аргументами: date, description, from_name, from_number_hidden, to_name,
    to_number_hidden, amount, currency_name.
    """

    def __init__(self, id, state, date, operationAmount, description, from_, to):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.from_ = from_
        self.to = to

        self.amount = ""
        self.currency_name = ""
        self.from_name = ""
        self.from_number_hidden = ""
        self.to_name = ""
        self.to_number_hidden = ""


    def date_conversion(self):
        """
        Преобразует формат даты
        """
        self.date = self.date.strftime("%d.%m.%Y")


    def define_amount(self):
        """
        Определяет аргумент amount
        """
        self.amount = self.operationAmount["amount"]


    def define_currency_name(self):
        """
        Определяет аргумент currency_name
        """
        self.currency_name = self.operationAmount["currency"]["name"]

    def define_from_name(self):
        """
        Определяет аргумент from_name
        """
        temporary = self.from_.split()[0:-1]
        if len(temporary) == 1:
            self.from_name = temporary[0]
        else:
            self.from_name = " ".join(temporary)


    def define_from_number_hidden(self):
        """
        Определяет аргумент from_number_hidden
        """
        temporary_1 = self.from_.split()[-1]
        temporary_2 = temporary_1[:6] + "******" + temporary_1[-4:]
        self.from_number_hidden = temporary_2[:4] + " " + temporary_2[4:8] + " "\
                                  + temporary_2[8:12] + " " + temporary_2[12:]


    def define_to_name(self):
        """
        Определяет аргумент to_name
        """
        temporary = self.to.split()[0:-1]
        if len(temporary) == 1:
            self.to_name = temporary[0]
        else:
            self.to_name = " ".join(temporary)


    def define_to_number_hidden(self):
        """
        Определяет аргумент to_number_hidden
        """
        temporary = self.to.split()[-1]
        self.to_number_hidden = "**" + temporary[-4:]


    def __repr__(self):
        return f"Output(date = '{self.date}', description = '{self.description}', from_name = '{self.from_name}'"\
               f"from_number_hidden = '{self.from_number_hidden}', to_name = '{self.to_name}', amount = '{self.amount}'"\
               f"to_number_hidden = '{self.to_number_hidden}', currency_name = '{self.currency_name}')"


