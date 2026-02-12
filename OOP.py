def double(x):

    return x*2

# Writea and defnie a python class and method
from abc import ABC, abstractmethod

class Invoice:
    def __init__(self, id, price,service):
        self.id = id 
        self.price = price 
        self.service = service


    def __str__(self):
        # This method must return a human-readable string
        return f"Id: {self.id}, Price: {self.price}, Service: {self.service}"



class InvoiceRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Invoice | None:
        pass

    @abstractmethod
    def save(self, invoice: Invoice) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[Invoice]:
        pass


class InMemoryUserRepository(InvoiceRepository):

    def __init__(self):
        self.invoice: dict[int, Invoice] = {}

    def list_all(self) -> list[Invoice]:
        return list(self.invoice.values())

    def get_by_id(self, id: int) -> Invoice | None:
        return self.invoice.get(id)

    def save(self, invoice: Invoice) -> None:
        self.invoice[invoice.id] = invoice

# Write  and defnie a service


class InvoiceService:
    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def list_all(self):
        return self.repository.list_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def create_invoice(self, id: int, price: float, service: str) -> Invoice:
        # regla de negocio
        if self.repository.get_by_id(id):
            raise ValueError("Invoice already exists")

        invoice = Invoice(id, price, service)
        self.repository.save(invoice)
        return invoice

# Write and defnie a controller or router

# Write and defnie a decorator

# Write and defnie a comprehension list

# Write and defnie a generator

# Write and defnie a closure

# Write and defnie a lamba

# Write and defenie magic methos in python


if __name__  == '__main__':

    repository = InMemoryUserRepository()
    service = InvoiceService(repository)
    invoice1 = service.create_invoice(1,200, 'Whatsapp')
    invoice2 = service.create_invoice(2,300,'Whastapp')

    # print(service.list_all())
    for invoice  in service.list_all():
        print(invoice)

    service.get_by_id(1)