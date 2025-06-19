"""Ejercicio 2: Simulador de préstamo con sistema francés
Enunciado:
Modelá una clase Prestamo que calcule el valor de la cuota mensual de un préstamo bajo el sistema francés de amortización, usando como datos:

Capital solicitado.

Tasa de interés anual.

Cantidad de cuotas.

La clase debe:

Calcular el valor fijo de la cuota.

Mostrar un plan de pagos mensual, detallando: número de cuota, monto total, capital amortizado, interés pagado y saldo restante.

"""

class Prestamo:
    def __init__(self, capital, tasa, cuota):
        self.capital = capital
        self.tasa = tasa
        self.cuota = cuota

    def calculo_cuota(self, capital, tasa, cuota):
        t = (tasa/12)/100
        valor_cuota = capital * (t * (1 + t) ** cuota) / ((1 + t) ** cuota - 1)
        return valor_cuota
    
    def mostrar_plan(self):
        saldo = self.capital
        t = (self.tasa/12)/100
        print(f"{'\tCuota':} {'\tTotal':} {'\tCapital':} {'\tInterés':} {'\tSaldo':}")
        for i in range(1, self.cuota + 1):
            interes = saldo * t
            capital_amortizado =  - interes
            saldo -= capital_amortizado
        print(f"{i:5d} {self.cuota_mensual:12.2f} {capital_amortizado:12.2f} {interes:12.2f} {max(saldo,0):12.2f}")

prestamo_1 = Prestamo(10000, 60, 12)
print(f"Cuota mensual: {prestamo_1.calculo_cuota(10000, 60, 12):.2f}")




 



