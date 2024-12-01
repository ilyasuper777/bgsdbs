Cisco работает на основе Cisco IOS. Взаимодействие с ОС возможно через SSH, telnet и консольный кабель. <br>
Практически вссе команды можно узнать с помощью команды ? <br>
Большинство команд, которые нам интересны с точки зрения парсинга делаются с попощью команды show <br>
<br>
Введём в терминале: `Router#show ?` <br>
Вывод: <br>
![<b>img1</b>](./img/img1.png)
Отсюда, например, можно понять, что версию Cisco IOS можжно узнать с помощью `show version`. <br>
Узнать таблицу MAC-адресов можно с помощью команды `show mac`. <br> Вывод: <br>

```
Vlan Mac Address Type Ports

—- ———– ——– —–

55 00a1.b2c3.d4e5 DYNAMIC Fa0/1
77 00b2.c3d4.e5f6 STATIC Fa0/2
```

Узнать правила acl можно с помощью команды `show access-lists`. <br> Вывод: <br>

```
Standard IP access list 2
    10 permit any
```

Узнать правила nat можно с помощью команды `show ip nat translations`. <br> Вывод: <br>

```
Pro 	Inside global 	Inside local 	Outside local 	  Outside global
--- 	208.165.100.5	192.168.1.5	208.165.100.70  208.165.100.70
```

Основная команда, чтобы узнать о vrf: `show ip vrf` . <br>
Вывод: <br>

```
 Name             Default RD          Interfaces
 Company-A        <not set>           Fa0/0.81
 Company-B        <not set>           Fa0/0.82
```
