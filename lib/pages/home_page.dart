import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter_application_2/Tabs/Pancakes_tab.dart';
import 'package:flutter_application_2/Tabs/burguer_tab.dart';
import 'package:flutter_application_2/Tabs/donout_tab.dart';
import 'package:flutter_application_2/Tabs/pizza_tab.dart';
import 'package:flutter_application_2/Tabs/smoothie_tab.dart';
import 'package:flutter_application_2/utils/my_tab.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  List<Widget>  myTabs = [
    const MyTab(iconPath: 'lib/assets/donut.png'),
    const MyTab(iconPath: 'lib/assets/burger.png'),
    const MyTab(iconPath: 'lib/assets/burger.png'),
    const MyTab(iconPath: 'lib/assets/burger.png'),
    const MyTab(iconPath: 'lib/assets/pizza.png'),

  ];

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: myTabs.length,
      child: Scaffold(
        appBar: AppBar( 
          backgroundColor: Colors.transparent,
          //Icono Izquierdo
          leading: Icon(
          Icons.menu,
          color: Colors.grey[800]
          ),
          //Icono Derecho
          actions:const [
            Padding(
              padding: EdgeInsets.only(right: 24.0),
              child: Icon(Icons.person),
            )
          ],
        ),
        body: Column(
          children: [
        //Texto principal
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 36, vertical: 18),
            child: Row(
              children: [
                Text("I wan to  ", 
                style: TextStyle(
                  //Tamaño de letra
                  fontSize: 34
                )
                ),
                Text("Eat", 
                style: TextStyle(
                  //Tamaño de letra
                  fontSize: 32,
                  //Negritas
                  fontWeight: FontWeight.bold,
                  //Subrayado
                  decoration: TextDecoration.underline
                ),)
              ],
            ),
          ),
      
      
        //Pestaña (TaBar)
        TabBar(tabs: myTabs),
        Expanded(child: TabBarView(children: [DonutTab(), BurguerTab(), SmoothieTab(), PancakesTab(), PizzaTab(),])),
        //Contenido(Cart)
      
          ],)
      ),
    );
  }
}