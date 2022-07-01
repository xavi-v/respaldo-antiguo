# simule un cajero
# saldo inicial 1.000
# menú:
# ▲ingresar dinero #▼retirar dinero #♠saldo #■salir

print("bienvenido a su cajero")
print("╔═══════════════════════╗")
print("║ $$ Seleccione su menú ║")
print("║___digite una letra____║")
print("║  ▲ingresar dinero = i ║")
print("║  ▼retirar $       = r ║")
print("║  ♠saldo disponile = s ║")
print("║  ■salir           = e ║")
menu = (input("║ >>digite opcion:")).lower()

saldo = 1000

if menu == "i":
    deposito = int(input("║ingrese monto:"))
    saldo += deposito
    print(f"║Saldo actual:{saldo}      ║")

elif menu == "r":
    retiro = int(input("║cuanto desea retirar:"))
    if retiro>saldo:
        print("║no hay suficiente saldo║")
    else:
        saldo -= retiro
        print(f"Saldo actual:{saldo}")

elif menu == "s":
    print(f"║saldo: {saldo}             ║")


elif menu == "e":
    print("║■  vuelva  pronto !!!  ║")

else:
    print("║opcion invalida ERROR!!║")
print("╚═══════════════════════╝")
