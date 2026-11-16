import json
import csv
import re

raw_data_text = """Base de datos final Línea Azul,,,,,,,
Celda vacía = no participó en esa instancia.,,,,,,,
,,,,,,,
Nombre,Colegio,Challwa PRE (0-9),Challwa POST (0-9),Challwa mejoró,Desierto Azul cumple KPI,DA Δ,Encuesta Climatón
Alan Erazo Cuero,Escuela Claudio Matte Pérez,3,8,SI,SI,2,—
Alonso Cárdenas Cabrera,Escuela Claudio Matte Pérez,1,2,SI,SI,1,SI
Antonia Negrete Pastén,Escuela Claudio Matte Pérez,3,5,SI,SI,2,—
Ariana Morales Alpaca,Escuela Claudio Matte Pérez,2,5,SI,SI,2,SI
Cristopher Padrón Cárdenas,Escuela Claudio Matte Pérez,2,8,SI,SI,1,SI
Janely Rodríguez Hernández,Escuela Claudio Matte Pérez,1,5,SI,NO,0,SI
José Arando Jiménez,Escuela Claudio Matte Pérez,1,2,SI,SI,1,SI
Luciana Urapiante Bilbao,Escuela Claudio Matte Pérez,1,9,SI,SI,2,SI
Nahuel Prieto Campillay,Escuela Claudio Matte Pérez,4,5,SI,NO,0,SI
Ángel Vera Forero,Escuela Claudio Matte Pérez,2,5,SI,NO,0,SI
Alfonso Araos Torrejón,Escuela Ecológica Humberto González Echegoyen,7,7,=,SI,1,SI
Cristopher Salazar Medero,Escuela Ecológica Humberto González Echegoyen,1,6,SI,NO,0,SI
Emilia Ahumada Araya,Escuela Ecológica Humberto González Echegoyen,4,8,SI,NO,0,SI
Emily Manríquez Villegas,Escuela Ecológica Humberto González Echegoyen,—,—,—,SI,1,SI
Javiera Paredes Jackson,Escuela Ecológica Humberto González Echegoyen,6,5,NO,NO,-1,SI
Kendra Calderón Viacava,Escuela Ecológica Humberto González Echegoyen,7,6,NO,—,—,SI
Lia Kong Villafuente,Escuela Ecológica Humberto González Echegoyen,—,—,—,NO,0,SI
Matias Roda Olivares,Escuela Ecológica Humberto González Echegoyen,8,8,=,NO,0,SI
Maximiliano Cortés Barrios,Escuela Ecológica Humberto González Echegoyen,5,3,NO,NO,0,SI
Máximo Alvarado Gordillo,Escuela Ecológica Humberto González Echegoyen,3,5,SI,NO,0,SI
Antonella Espinoza Manuelda,Escuela Ecológica Padre Alberto Hurtado,6,9,SI,NO,0,—
Emily Sandoval Sandoval,Escuela Ecológica Padre Alberto Hurtado,—,—,—,—,—,—
Janain Jimenez Delgadillo,Escuela Ecológica Padre Alberto Hurtado,—,—,—,—,—,—
Madeleyn Ibaer Báez,Escuela Ecológica Padre Alberto Hurtado,—,—,—,—,—,—
María Paz Amira Valencia,Escuela Ecológica Padre Alberto Hurtado,3,8,SI,SI,1,—
Roberto Ledezma Cuturrufo,Escuela Ecológica Padre Alberto Hurtado,2,7,SI,NO,0,—
Selena Oros Riquelme,Escuela Ecológica Padre Alberto Hurtado,—,—,—,—,—,—
Sofía Araos Bueno,Escuela Ecológica Padre Alberto Hurtado,3,6,SI,NO,0,—
Sofía Mella,Escuela Ecológica Padre Alberto Hurtado,3,5,SI,NO,0,—
Álvaro Vargas,Escuela Ecológica Padre Alberto Hurtado,2,7,SI,SI,1,—
Aymeet Cueva Opazo,Escuela Javiera Carrera,2,6,SI,—,—,—
Esteban Guerra Calle,Escuela Javiera Carrera,3,7,SI,NO,-1,—
Hugo Molina Naranjo,Escuela Javiera Carrera,2,6,SI,NO,-1,—
Jeremy Marín Jiménez,Escuela Javiera Carrera,—,—,—,SI,1,—
León Chang Riveros,Escuela Javiera Carrera,2,2,=,SI,2,—
Roben Díaz Condori,Escuela Javiera Carrera,2,4,SI,SI,2,—
Sebastián Salazar Tapia,Escuela Javiera Carrera,7,9,SI,SI,2,—
Valery Cáceres Meneses,Escuela Javiera Carrera,1,6,SI,SI,1,—
Aliz Mollericona Ticona,Escuela Juan Pablo II,3,7,SI,SI,1,—
Ana Campos,Escuela Juan Pablo II,1,5,SI,SI,1,—
Anaís Rojas Cheuquepán,Escuela Juan Pablo II,—,—,—,SI,1,—
Emilia Marín Castillo,Escuela Juan Pablo II,4,5,SI,SI,2,—
Erik Serrano,Escuela Juan Pablo II,2,4,SI,SI,1,—
Juan Sánchez Valencia,Escuela Juan Pablo II,4,4,=,NO,0,—
Mateo Torres Quispe,Escuela Juan Pablo II,3,9,SI,SI,1,—
Nadriel Vaca Suárez,Escuela Juan Pablo II,4,6,SI,NO,0,—
Patricio Chandía González,Escuela Juan Pablo II,4,6,SI,SI,1,—
Aron Ardiles Vega,Escuela República de Estados Unidos,3,6,SI,SI,1,SI
Aylynn Opazo Carvajal,Escuela República de Estados Unidos,4,8,SI,SI,2,SI
Berenice Jora Zarate,Escuela República de Estados Unidos,1,2,SI,—,—,SI
Evelyn Estigarribia Choquecota,Escuela República de Estados Unidos,5,5,=,NO,0,SI
Jorge Seas Tomicha,Escuela República de Estados Unidos,3,3,=,NO,0,SI
Keyla Morán González,Escuela República de Estados Unidos,5,8,SI,NO,0,SI
Lucas Llanqui Honorio,Escuela República de Estados Unidos,5,7,SI,NO,-1,SI
Matías Orellana Flores,Escuela República de Estados Unidos,6,7,SI,SI,1,SI
Minzy Díaz Vergara,Escuela República de Estados Unidos,4,8,SI,SI,2,SI
Ariatna Herrera Caicedo,Escuela República de Italia,5,5,=,NO,0,SI
Arshiel Gronchi Martínez,Escuela República de Italia,3,6,SI,SI,1,SI
Emilia Narváez Narváez,Escuela República de Italia,3,1,NO,SI,1,—
Fernando Aros Santus,Escuela República de Italia,7,9,SI,—,—,SI
Jesús Rivero Velásquez,Escuela República de Italia,1,5,SI,SI,1,—
José Rivero Velásquez,Escuela República de Italia,1,4,SI,SI,1,SI
Kiara Carvajal Mondaca,Escuela República de Italia,2,2,=,NO,0,SI
María Rementería Ardiles,Escuela República de Italia,4,3,NO,NO,0,SI
Nicol Palacios Cruz,Escuela República de Italia,5,5,=,SI,2,SI
Thais Opazo Ovando,Escuela República de Italia,2,2,=,SI,2,SI
Antonella Ruiz Fritis,Liceo Domingo Herrera Rivera,3,6,SI,SI,1,SI
Belén Dubost Alfaro,Liceo Domingo Herrera Rivera,4,5,SI,NO,0,SI
Daliha Orellana Humaña,Liceo Domingo Herrera Rivera,4,5,SI,SI,1,SI
Ignacia Reyes Yau,Liceo Domingo Herrera Rivera,2,4,SI,—,—,—
Juan Talamilla Jiménez,Liceo Domingo Herrera Rivera,4,8,SI,SI,1,SI
Matías Gálvez Gaete,Liceo Domingo Herrera Rivera,2,5,SI,SI,1,SI
Máximo Díaz López,Liceo Domingo Herrera Rivera,1,0,NO,NO,-1,SI
Oscar Araya Núñez,Liceo Domingo Herrera Rivera,—,—,—,—,—,—
Sharon Guaitoto Duque,Liceo Domingo Herrera Rivera,5,7,SI,—,—,SI
Thiago Cayuba Magueño,Liceo Domingo Herrera Rivera,2,6,SI,SI,1,SI
"""

with open("E:/dashboard_linea_azul/raw_base_final.txt", "w", encoding="utf-8") as f:
    f.write(raw_data_text)

print("Base final guardada")
