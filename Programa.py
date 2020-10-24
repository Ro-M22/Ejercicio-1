from Email import Email
from ManejadorEmail import ManejadorEmails

if __name__ == '__main__':
    ###########################################PUNTO1 IMPLENTACION########################
    print('                          PROGRAMA PRINCIPAL: Ejercicio1')
    print('1-Ingrese los siguientes Datos')
    nombre = input('NOMBRE: ')
    idcuenta= input("Id de la cuenta: ")
    dominio=input("Dominio: ")
    tipoDominio=input("Tipo Dominio: ")
    contraseña=input("Contraseña: ")
    otroEmail = Email(idcuenta, dominio, tipoDominio, contraseña)
    print('Estimado/a {}, te enviaremos los mensajes a la dirección: {}\n '.format(nombre, otroEmail.retornaEmail()))
    print("2- Ingrese su contraseña actual")
    passw= input()
    if (otroEmail.verificaContraseña(passw)):
        print("Ingrese su nueva contraseña")
        otroEmail.setContraseña( input())
    else:
        print("Contraseña incorrecta")
    print(otroEmail.getContraseña())

    print('3- AHORA LEEMOS CORREOS DENTRO DEL ARCHIVO')
    m = ManejadorEmails()
    m.testEmails()

    dom = input("4- Ingrese el dominio a buscar: ")
    cant = m.buscarEmailDominio(dom)
    print('Cantidad de Emails con Dominio "', dom, '" es: ', cant)

    print('\nFIN DEL PROGRAMA')

