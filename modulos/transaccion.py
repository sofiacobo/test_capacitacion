class Transaccion:

    def __init__(self, id, monto, moneda):
        self.id = id
        self.monto = monto
        self.moneda = moneda

    def validar(self):
        if self.monto <= 0:
            return "Monto inválido"
        elif self.moneda == "ARS" and self.monto > 100000:
            return "Requiere autorización adicional"
        elif self.moneda == "USD" and self.monto > 10000:
            return "Requiere autorización adicional por monto en divisa USD"
        else:
            return "Transacción válida"
        
    def __str__(self):
        return f"ID: {self.id} | Monto: {self.monto} | Moneda: {self.moneda}"
    
