import csv

desierto_azul_respuestas_raw = """Nombre oficial,Colegio,Q1 PRE,Q2 PRE,Q3 PRE,Q4 tipos basura (PRE),Q5 acción (PRE),B1 POST,B2 POST,B3 POST,B4 basura+acción (POST),B5 qué sorprendió (POST)
Alan Erazo Cuero,Escuela Claudio Matte Pérez,d,a,a,bolsas; botellas; redes,recoger la basura de la playa,d,d,a,botellas y colillas; la puedo disminuir limpiando las playas,las conchas y la cantidad de diversas conchas
Alonso Cárdenas Cabrera,Escuela Claudio Matte Pérez,e,a,a,plasticos,no se,e,a,a,cigarros y botellas,(ilegible)
Antonia Negrete Pastén,Escuela Claudio Matte Pérez,a,d,a,botellas; bolsas; palos de paleta,botar mi basura,d,d,a,bolsas y colilla de cigarro,que tienen mucha basura para reciclar
Ariana Morales Alpaca,Escuela Claudio Matte Pérez,d,a,a,botellas; bolsas de plastico,no tirar basura al mar,d,d,a,botellas; bolsas; toallas; botellas de bebida; cigarro; carbon,"de que hay muchos tipos de conchas de mar, porque estaban lindas"
Cristopher Padrón Cárdenas,Escuela Claudio Matte Pérez,d,a,a,botellas de agua; bolsas de basura; otras bolsas,no botar basura al mar,d,d,a,bolsas plasticas y botellas,todas las cosas porque son muy interesantes
Janely Rodríguez Hernández,Escuela Claudio Matte Pérez,a,a/d,a,bolsas de basura; botellas plasticas,botar la basura en el basurero,a,b,a,plasticos,los caracoles porque estan bonitos
José Arando Jiménez,Escuela Claudio Matte Pérez,e,d,b,bolsas; etc,hacer contenedores,c,d,d,cigarro y tapas de botellas,una playa
Luciana Urapiante Bilbao,Escuela Claudio Matte Pérez,a,d,a,los plasticos y bolsas,tener basureros en las playas,d,d,a,colilla; plastico y bolsa,fue la cantidad de cosas marinas que no conocia
Nahuel Prieto Campillay,Escuela Claudio Matte Pérez,a,d,a,bolsas y botellas,"(tachado, ilegible)",a,d,a,bolsas y botellas de plastico,cuidar el medio ambiente y el tipo de conchas
Ángel Vera Forero,Escuela Claudio Matte Pérez,a,d,a,botellas de plastico; bolsas de plastico,no botar basura en las playas,a,d,a,botellas y muchas bolsas,lo que hacen porque son sorprendentes
Alfonso Araos Torrejón,Escuela Ecológica Humberto González Echegoyen,b,a/d,a,bolsas de plasticos; botellas; redes; colillas,no botando las basuras a los mares y lagos,b,d,a,cigarro; botellas; papel; vidrio; madera; colillas; no botando basura,la cantidad de colillas y cigarros que he encontrado
Cristopher Salazar Medero,Escuela Ecológica Humberto González Echegoyen,a,d,a,botellas; bolsas plasticas; colillas de cigarro,cuando encuentro basura la recojo; la pongo en una bolsa y en mi casa la boto,a,d,a,botellas; cigarros; poner en una bolsa para llevar mi basura,me sorprendio todo porque no me imaginaba todo lo que iba a ver con mis ojos
Emilia Ahumada Araya,Escuela Ecológica Humberto González Echegoyen,d,d,a,bolsas; cigarros; botellas; envoltorios,no dejar la basura en la arena,d,d,a,botellas; bolsas; cigarros y plasticos,las actividades y lo de la ballena Anita
Emily Manríquez Villegas,Escuela Ecológica Humberto González Echegoyen,d,d,a,vidrios; redes de pesca; basura de comida,hablar y no botar basura,d,d,a,carbon y cigarrillos; cuando pueda la recoge,de lo bien que se expresan para invitar que cuiden el mar y las playas
Javiera Paredes Jackson,Escuela Ecológica Humberto González Echegoyen,d,d,a,botellas; bolsas; colillas; cigarros,no se,d,d,a,plastico; madera; unos basureros,porque era muy grande y tenia suciedad; habian demasiadas cosas
Lia Kong Villafuente,Escuela Ecológica Humberto González Echegoyen,a,a,a,botella; plastico; vidrio; metal; latas,poner contenedores; no actividades con basurales; sacar basura del mar,a,a,a,botella; lata; bolsas; hilos; vidrio,poner contenedores de basura y poner que votar basura a la calle es ilegal
Matias Roda Olivares,Escuela Ecológica Humberto González Echegoyen,d,d,a,cigarro; redes plasticas; anzuelos; envoltorios; cajas de jugo; botellas; tapas,traer bolsas de basura y botarla en la casa,d,d,a,cigarros; cajas de jugo; botarlo en una bolsa,las diferentes especies que hay en las playas
Maximiliano Cortés Barrios,Escuela Ecológica Humberto González Echegoyen,a,d,a,botellas; bolsas; redes; cigarro,poner carteles de no echar basura,d,d,a,botella plastica; botandola a la basura,lo que cuidan el lugar
Máximo Alvarado Gordillo,Escuela Ecológica Humberto González Echegoyen,a,a,a,plastico; cristal,botar basura en los basureros,a,a,a,cristal; plastico; no botarlo al agua,la aleta de ballena porque es un animal muy grande
Antonella Espinoza Manuelda,Escuela Ecológica Padre Alberto Hurtado,d,d,a,plasticos; cigarros; vidrios; ropa abandonada,recoger la basura que encuentro y no botarla,d,d,a,cigarros; botellas de alcohol; puedo ayudar limpiando las playas,me sorprendio todas las colillas de cigarros que han reciclado
María Paz Amira Valencia,Escuela Ecológica Padre Alberto Hurtado,d,d,a,redes de pesca; botellas; cosas plasticas,utilizar menos plastico y botarlas en los basureros,d,d,a,cigarros; plastico; metal,la cantidad de basura que sale de un cuadrado y el tamano de las tortugas
Roberto Ledezma Cuturrufo,Escuela Ecológica Padre Alberto Hurtado,d,c,a,plasticos; botellas; redes,poder crear algo para sacar la basura marina,c,a,a,colillas; plasticos; vidrios; recolectarlas y reciclar,me sorprendio que habian conchas que brillaban
Sofía Araos Bueno,Escuela Ecológica Padre Alberto Hurtado,d,d,a,plastico; bolsas; latas,recoger la basura de las playas y mar,d,d,a,tapas de cerveza; bolsas; dejar de tomar y guardar las bolsas,me sorprendio las esculturas porque estan hechas con residuos
Sofía Mella,Escuela Ecológica Padre Alberto Hurtado,c,d,a,vidrio; bolsas; cigarro,sin contener vidrio y que saquen la basura,c,d,a,cigarros; botellas; colillas,los millones que hay en los cigarrillos
Álvaro Vargas,Escuela Ecológica Padre Alberto Hurtado,d,a,a,bolsas; papeles; vasos; plasticos,llevarme la basura y no contaminando,d,a,a,plasticos y colillas,las especies de animales marinos y formas
Esteban Guerra Calle,Escuela Javiera Carrera,d,d,a,cigarro; botellas; tapas; bolsas; vidrio,botando la basura,d,d,a,bolsas y tapas; no botar basura,lo que me sorprendio era que las conchas importan
Hugo Molina Naranjo,Escuela Javiera Carrera,c,a,a,vasos; bolsas; tapas; colillas,recoger basura; no contaminar,c,c,a,madera; bolsas,(tachado) de las cosas marinas
Jeremy Marín Jiménez,Escuela Javiera Carrera,a,a,a,plastico; caja de jugo; papeles,poner basureros; no botar plastico,c,b,a,cigarro; plastico; no llevar plastico,cuando buscamos especies
León Chang Riveros,Escuela Javiera Carrera,e,c,a,botella,recoger la basura de la playa,d,d,a,botellas,llevar una bolsa de basura
Roben Díaz Condori,Escuela Javiera Carrera,a,a,a,latas; plastico,no botar basura al mar,a,d,a,cigarros; vidrios; plastico; no botar basura en las playas,me sorprendio el sol del mar porque nunca he visto un sol de mar
Sebastián Salazar Tapia,Escuela Javiera Carrera,d,c,a,ropa; plastico; anzuelos,recogiendo basura de la playa,d,d,a,cigarro; botellas y recoger basura y reciclar,los organismos marinos y animales
Valery Cáceres Meneses,Escuela Javiera Carrera,a,a,a,bolsas de plastico; kapo; envoltorio de papas fritas; polera,evitando tirar basura; recogiendo lo de la calle; ir con una bolsa,a,b,a,bolsas plasticas; botellas; colillas; envoltorios; ropa; carbon,"de la historia de la ballena, el perrito Oso, que las colillas de cigarro son muy peligrosas"
Aliz Mollericona Ticona,Escuela Juan Pablo II,d,d,a,bolsas plasticas; botellas,ayudar a no contaminar,d,d,a,cigarro; plasticos; vidrios; tapa de botellas; metales,la cantidad de especies marinos y sus cualidades son asombrosas
Ana Campos,Escuela Juan Pablo II,d,d,a,botellas plasticas; empaques de galletas o papas,botar la basura en los basureros,d,d,a,cigarros; plasticos; podemos botar las cosas en el basurero,me sorprendio la cantidad de basura y las especies de los animales o rocas
Anaís Rojas Cheuquepán,Escuela Juan Pablo II,e,d,a,botellas; cigarros; bolsas plasticas; redes,carteles o basureros con animales que digan alimentame; recoger la basura,d,d,a,plastico; tapas; cigarrillos; vidrios; carbon,"por las cosas que habian, la mayoria de personas que botan basura"
Emilia Marín Castillo,Escuela Juan Pablo II,d,a/d,d,bolsas; botellas,poner botes de basura y tener letrero,d,d,c,plasticos; cigarro,(ilegible)
Erik Serrano,Escuela Juan Pablo II,d,c,a,balde de basura; botellas; plastico,no botar la basura al mar,d,d,a,plastico; botellas; las latas al basurero o reciclar,"lo que estan haciendo, reciclan las colillas de cigarrillos"
Juan Sánchez Valencia,Escuela Juan Pablo II,a,a,a,botella; plastico; red de pesca,no botar basura,a,a,a,botellas y redes de pesca,que debemos cuidar el mar
Mateo Torres Quispe,Escuela Juan Pablo II,a,d,a,botellas y bolsas,botar la basura de la playa en el basurero,d,a,a,cigarros; plastico; vidrio,las cosas hechas de cigarro porque tienen muchos cigarros reciclados
Nadriel Vaca Suárez,Escuela Juan Pablo II,d,d,a,de las actividades realizadas pesca y agricultura (fuera de tema),hacer carteles o contenedores para su tipo de residuos,d,d,a,de actividades realizadas en tierra y la pesca y acuicultura / carteles o contenedores,lo que me gusto fue venir
Patricio Chandía González,Escuela Juan Pablo II,d,d,a,botellas; redes de plastico,pueden poner una multa por botar basura en playa,d,d,a,colillas de cigarros; tapas de botellas,me sorprendio que somos la region mas (¿cochina?)
Aron Ardiles Vega,Escuela República de Estados Unidos,d,d,a,botellas; vidrios; bolsa de basura,recoger la basura,d,d,a,botellas; colillas de cigarro; bolsa de basura,que vemos que nuestro alrededor hay mucha basura
Aylynn Opazo Carvajal,Escuela República de Estados Unidos,a,d,a,botella; bolsas de basura; vidrios,recoger la basura,d,d,a,botellas; colillas de cigarro,de que hay muchas colillas de cigarro
Evelyn Estigarribia Choquecota,Escuela República de Estados Unidos,d,d,a,botellas plasticas; envoltorios de comida; bolsas plasticas,no botar basura al mar,a,d,a,colillas de cigarro y huesos; no ensuciar,"habia mucha basura, jamas habia visto tanta basura"
Jorge Seas Tomicha,Escuela República de Estados Unidos,a/d,d,d,plastico; botella; mantel,no se,a,d,d,no se,es bonito y disfrute el lugar y etc
Keyla Morán González,Escuela República de Estados Unidos,d,d,a,botellas; residuos de comida; vidrio; bolsas,no contaminar,d,d,a,vidrio; plastico; no botarlas en las playas,me sorprendio las actividades. Muy bonito
Lucas Llanqui Honorio,Escuela República de Estados Unidos,b,d,a,cigarros; botellas de vidrio,personas que se queden en la playa para decir que no boten basura,a,a,a,plastico y cigarros,recoger conchas
Matías Orellana Flores,Escuela República de Estados Unidos,d,d,a,plasticos; botellas; madera,reciclar,d,d,a,colillas; plastico; madera; corcho; huesos,tira un erizo y me saque una foto con el
Minzy Díaz Vergara,Escuela República de Estados Unidos,d,a,a,botellas; plastico; panales,no botar basura a la playa y recoger la basura,d,d,a,botellas; colillas de cigarro; vidrio; tratar de recoger basura,porque hay mucha basura en Antofagasta
Ariatna Herrera Caicedo,Escuela República de Italia,d,c,a,cigarro y bolsas,recogiendo la basura,a,d,a,cigarro; metal; papel; plastico; ceramica,todo lo que hicimos por el mar
Arshiel Gronchi Martínez,Escuela República de Italia,d,c,a,botellas; panales; bolsas,que las personas recojan sus basuras,a,d,a,papel; plastico; ceramica; metal y cigarro,todo lo que hicimos por el oceano
Emilia Narváez Narváez,Escuela República de Italia,e,c,a,botellas de plastico,recoger la basura que la gente tira,c,b,a,cigarrillos; tapas,la ballena Anita
Jesús Rivero Velásquez,Escuela República de Italia,d,d,a,plastico,no se,d,d,a,colilla de cigarro; tapa de cerveza,que los cigarros echan de basura
José Rivero Velásquez,Escuela República de Italia,d,d,a,bolsas plastico; botellas de plastico; restos de comida,limpiar y reciclar los residuos,d,d,a,cigarrillos; botellas plasticas; bolsas,"me sorprendio la cantidad de especies marinas alli, mucha variedad"
Kiara Carvajal Mondaca,Escuela República de Italia,d,d,a,cosas de plastico,sacar toda la basura,d,d,a,cosas de plasticos o de metal,las costillas de las ballenas
María Rementería Ardiles,Escuela República de Italia,a,c,a,cigarro; bolsas; papel; botella,"cuidar, botar la basura",c,b,a,colillas; tapas de cerveza; vidrio,lo del mar o no se
Nicol Palacios Cruz,Escuela República de Italia,a,a,a,bolsas plasticas y botellas,no botando mas basura,d,a,a,colillas de cigarros; botellas de plastico; vasos,la cantidad de basura porque no pensaba que hubiera tanto
Thais Opazo Ovando,Escuela República de Italia,d,a,d,bolsas; basura; botellas,limpiar la playa,d,d,d,colillas; bolsas; botellas,me sorprendio los pepinos de mar
Antonella Ruiz Fritis,Liceo Domingo Herrera Rivera,a,d,a,cigarros; bolsas; latas; vidrio; metal; plastico,limpiar o llevar una bolsa para la basura,d,d,a,carbon; cigarros; bolsas; basureros o traer una bolsa para la basura,de que Antofagasta es la ciudad con la playa mas sucia de Chile
Belén Dubost Alfaro,Liceo Domingo Herrera Rivera,a,d,a,botellas; tapas; plastico; redes,poner basureros cerca,a,b,a,las colillas y vidrio; poner basureros,(en blanco)
Daliha Orellana Humaña,Liceo Domingo Herrera Rivera,b,d,a,colillas; redes; botellas; plasticos; vidrio; tapas,la verdad no se,d,d,a,dejar de tirar basura; colillas; alambre; botellas; plastico,"todas las especies marinas existentes, porque son muchas y todas muy diferentes"
Juan Talamilla Jiménez,Liceo Domingo Herrera Rivera,d,d,a,bolsas plasticas; botellas plasticas; redes,juntar a un grupo de gente para que recojan la basura y la boten,d,d,a,cigarros; carbon; botellas plasticas; bolsas; papeles,"que de vez en cuando viene una ballena, sus 3 novios y un bebe"
Matías Gálvez Gaete,Liceo Domingo Herrera Rivera,c,a,a,la botella; plastico; bolsas,recogerla,c,c,a,cigarrillos; vidrio; plastico y papel,que nosotros somos la primera ciudad mas con basura en Chile
Máximo Díaz López,Liceo Domingo Herrera Rivera,d,d,a,botellas; plasticos; latas,(ilegible),d,d,d,no se,no se
Sharon Guaitoto Duque,Liceo Domingo Herrera Rivera,a,c,a,bolsas; colillas de cigarro; plasticos,recoger la basura,,,,,
Thiago Cayuba Magueño,Liceo Domingo Herrera Rivera,d,d,a,redes de pesca; botellas; papeles; vidrio,no botar tanta basura,d,d,a,cigarrillos; vidrio; no botar tanta basura,"lo que hacen y como lo hacen, porque es interesante" """

desierto_azul_puntajes_raw = """Nombre oficial,Colegio,D1 PRE (0-3),D1 POST (0-3),Colillas PRE,Colillas POST,KPI PRE (0-4),KPI POST (0-4),Δ,Cumple KPI
Alan Erazo Cuero,Escuela Claudio Matte Pérez,2,3,0,1,2,4,2,SI
Alonso Cárdenas Cabrera,Escuela Claudio Matte Pérez,1,1,0,1,1,2,1,SI
Antonia Negrete Pastén,Escuela Claudio Matte Pérez,2,3,0,1,2,4,2,SI
Ariana Morales Alpaca,Escuela Claudio Matte Pérez,2,3,0,1,2,4,2,SI
Cristopher Padrón Cárdenas,Escuela Claudio Matte Pérez,2,3,0,0,2,3,1,SI
Janely Rodríguez Hernández,Escuela Claudio Matte Pérez,1,1,0,0,1,1,0,NO
José Arando Jiménez,Escuela Claudio Matte Pérez,1,1,0,1,1,2,1,SI
Luciana Urapiante Bilbao,Escuela Claudio Matte Pérez,2,3,0,1,2,4,2,SI
Nahuel Prieto Campillay,Escuela Claudio Matte Pérez,2,2,0,0,2,2,0,NO
Ángel Vera Forero,Escuela Claudio Matte Pérez,2,2,0,0,2,2,0,NO
Alfonso Araos Torrejón,Escuela Ecológica Humberto González Echegoyen,1,2,1,1,2,3,1,SI
Cristopher Salazar Medero,Escuela Ecológica Humberto González Echegoyen,2,2,1,1,3,3,0,NO
Emilia Ahumada Araya,Escuela Ecológica Humberto González Echegoyen,3,3,1,1,4,4,0,NO
Emily Manríquez Villegas,Escuela Ecológica Humberto González Echegoyen,3,3,0,1,3,4,1,SI
Javiera Paredes Jackson,Escuela Ecológica Humberto González Echegoyen,3,3,1,0,4,3,-1,NO
Lia Kong Villafuente,Escuela Ecológica Humberto González Echegoyen,1,1,0,0,1,1,0,NO
Matias Roda Olivares,Escuela Ecológica Humberto González Echegoyen,3,3,1,1,4,4,0,NO
Maximiliano Cortés Barrios,Escuela Ecológica Humberto González Echegoyen,2,3,1,0,3,3,0,NO
Máximo Alvarado Gordillo,Escuela Ecológica Humberto González Echegoyen,1,1,0,0,1,1,0,NO
Antonella Espinoza Manuelda,Escuela Ecológica Padre Alberto Hurtado,3,3,1,1,4,4,0,NO
María Paz Amira Valencia,Escuela Ecológica Padre Alberto Hurtado,3,3,0,1,3,4,1,SI
Roberto Ledezma Cuturrufo,Escuela Ecológica Padre Alberto Hurtado,2,1,0,1,2,2,0,NO
Sofía Araos Bueno,Escuela Ecológica Padre Alberto Hurtado,3,3,0,0,3,3,0,NO
Sofía Mella,Escuela Ecológica Padre Alberto Hurtado,2,2,1,1,3,3,0,NO
Álvaro Vargas,Escuela Ecológica Padre Alberto Hurtado,2,2,0,1,2,3,1,SI
Esteban Guerra Calle,Escuela Javiera Carrera,3,3,1,0,4,3,-1,NO
Hugo Molina Naranjo,Escuela Javiera Carrera,1,1,1,0,2,1,-1,NO
Jeremy Marín Jiménez,Escuela Javiera Carrera,1,1,0,1,1,2,1,SI
León Chang Riveros,Escuela Javiera Carrera,1,3,0,0,1,3,2,SI
Roben Díaz Condori,Escuela Javiera Carrera,1,2,0,1,1,3,2,SI
Sebastián Salazar Tapia,Escuela Javiera Carrera,2,3,0,1,2,4,2,SI
Valery Cáceres Meneses,Escuela Javiera Carrera,1,1,0,1,1,2,1,SI
Aliz Mollericona Ticona,Escuela Juan Pablo II,3,3,0,1,3,4,1,SI
Ana Campos,Escuela Juan Pablo II,3,3,0,1,3,4,1,SI
Anaís Rojas Cheuquepán,Escuela Juan Pablo II,2,3,1,1,3,4,1,SI
Emilia Marín Castillo,Escuela Juan Pablo II,1,2,0,1,1,3,2,SI
Erik Serrano,Escuela Juan Pablo II,2,3,0,0,2,3,1,SI
Juan Sánchez Valencia,Escuela Juan Pablo II,1,1,0,0,1,1,0,NO
Mateo Torres Quispe,Escuela Juan Pablo II,2,2,0,1,2,3,1,SI
Nadriel Vaca Suárez,Escuela Juan Pablo II,3,3,0,0,3,3,0,NO
Patricio Chandía González,Escuela Juan Pablo II,3,3,0,1,3,4,1,SI
Aron Ardiles Vega,Escuela República de Estados Unidos,3,3,0,1,3,4,1,SI
Aylynn Opazo Carvajal,Escuela República de Estados Unidos,2,3,0,1,2,4,2,SI
Evelyn Estigarribia Choquecota,Escuela República de Estados Unidos,3,2,0,1,3,3,0,NO
Jorge Seas Tomicha,Escuela República de Estados Unidos,1,1,0,0,1,1,0,NO
Keyla Morán González,Escuela República de Estados Unidos,3,3,0,0,3,3,0,NO
Lucas Llanqui Honorio,Escuela República de Estados Unidos,2,1,1,1,3,2,-1,NO
Matías Orellana Flores,Escuela República de Estados Unidos,3,3,0,1,3,4,1,SI
Minzy Díaz Vergara,Escuela República de Estados Unidos,2,3,0,1,2,4,2,SI
Ariatna Herrera Caicedo,Escuela República de Italia,2,2,1,1,3,3,0,NO
Arshiel Gronchi Martínez,Escuela República de Italia,2,2,0,1,2,3,1,SI
Emilia Narváez Narváez,Escuela República de Italia,1,1,0,1,1,2,1,SI
Jesús Rivero Velásquez,Escuela República de Italia,3,3,0,1,3,4,1,SI
José Rivero Velásquez,Escuela República de Italia,3,3,0,1,3,4,1,SI
Kiara Carvajal Mondaca,Escuela República de Italia,3,3,0,0,3,3,0,NO
María Rementería Ardiles,Escuela República de Italia,1,1,1,1,2,2,0,NO
Nicol Palacios Cruz,Escuela República de Italia,1,2,0,1,1,3,2,SI
Thais Opazo Ovando,Escuela República de Italia,1,2,0,1,1,3,2,SI
Antonella Ruiz Fritis,Liceo Domingo Herrera Rivera,2,3,1,1,3,4,1,SI
Belén Dubost Alfaro,Liceo Domingo Herrera Rivera,2,1,0,1,2,2,0,NO
Daliha Orellana Humaña,Liceo Domingo Herrera Rivera,2,3,1,1,3,4,1,SI
Juan Talamilla Jiménez,Liceo Domingo Herrera Rivera,3,3,0,1,3,4,1,SI
Matías Gálvez Gaete,Liceo Domingo Herrera Rivera,1,1,0,1,1,2,1,SI
Máximo Díaz López,Liceo Domingo Herrera Rivera,3,2,0,0,3,2,-1,NO
Sharon Guaitoto Duque,Liceo Domingo Herrera Rivera,1,,1,,2,,,
Thiago Cayuba Magueño,Liceo Domingo Herrera Rivera,3,3,0,1,3,4,1,SI"""

climaton_respuestas_raw = """Nombre oficial,Colegio,P1 Cuidar,P2 Puedo actuar,P3 Entiendo,P4 Ideas,P5 Prototipar,P6 Comunicar,P7 Me gustó,P8 Equipo,P9 Volver
Alonso Cárdenas Cabrera,Escuela Claudio Matte Pérez,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Ariana Morales Alpaca,Escuela Claudio Matte Pérez,Sí,Sí,Más o menos,Sí,Sí,Más o menos,Sí,Sí,Sí
Cristopher Padrón Cárdenas,Escuela Claudio Matte Pérez,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí,Sí
Janely Rodríguez Hernández,Escuela Claudio Matte Pérez,Sí,Sí,Sí,Más o menos,Sí,Más o menos,Sí,Sí,Sí
José Arando Jiménez,Escuela Claudio Matte Pérez,Sí,Más o menos,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Luciana Urapiante Bilbao,Escuela Claudio Matte Pérez,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Nahuel Prieto Campillay,Escuela Claudio Matte Pérez,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Ángel Vera Forero,Escuela Claudio Matte Pérez,Sí,Más o menos,Sí,Sí,Más o menos,Más o menos,Sí,Más o menos,Sí
Alfonso Araos Torrejón,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Cristopher Salazar Medero,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Más o menos,Sí,,Sí,Sí,Sí
Emilia Ahumada Araya,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Emily Manríquez Villegas,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Javiera Paredes Jackson,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Kendra Calderón Viacava,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Lia Kong Villafuente,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Matias Roda Olivares,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Maximiliano Cortés Barrios,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Máximo Alvarado Gordillo,Escuela Ecológica Humberto González Echegoyen,Sí,Sí,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí
Aron Ardiles Vega,Escuela República de Estados Unidos,Sí,Sí,Sí,Más o menos,Más o menos,Sí,Sí,Sí,Sí
Aylynn Opazo Carvajal,Escuela República de Estados Unidos,Sí,Más o menos,Sí,Más o menos,Sí,Sí,Sí,Más o menos,Sí
Berenice Jora Zarate,Escuela República de Estados Unidos,Sí,Más o menos,Sí,Sí,Sí,Más o menos,Sí,Más o menos,Más o menos
Evelyn Estigarribia Choquecota,Escuela República de Estados Unidos,Más o menos,Sí,Más o menos,Sí,Sí,Más o menos,Sí,Más o menos,Sí
Jorge Seas Tomicha,Escuela República de Estados Unidos,Sí,Más o menos,Sí,Más o menos,Sí,No,Sí,Más o menos,Más o menos
Keyla Morán González,Escuela República de Estados Unidos,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí,Sí
Lucas Llanqui Honorio,Escuela República de Estados Unidos,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Matías Orellana Flores,Escuela República de Estados Unidos,Sí,Más o menos,Más o menos,Más o menos,Más o menos,Sí,Sí,Sí,Sí
Minzy Díaz Vergara,Escuela República de Estados Unidos,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí,Sí
Ariatna Herrera Caicedo,Escuela República de Italia,Sí,Sí,Sí,,Sí,Sí,Sí,Sí,Sí
Arshiel Gronchi Martínez,Escuela República de Italia,Sí,Más o menos,Sí,No,Sí,No,Sí,Sí,Sí
Fernando Aros Santus,Escuela República de Italia,Sí,Sí,Sí,Sí,Más o menos,Más o menos,Sí,Sí,Sí
José Rivero Velásquez,Escuela República de Italia,Sí,Sí,Sí,Más o menos,No,Sí,Sí,Sí,Sí
Kiara Carvajal Mondaca,Escuela República de Italia,Sí,Sí,Sí,Más o menos,Más o menos,Sí,Sí,Sí,Sí
María Rementería Ardiles,Escuela República de Italia,Sí,Sí,Más o menos,Sí,Más o menos,Sí,Sí,Sí,Sí
Nicol Palacios Cruz,Escuela República de Italia,Sí,Más o menos,Sí,Más o menos,Sí,Más o menos,Sí,Sí,Sí
Thais Opazo Ovando,Escuela República de Italia,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí,Sí
Antonella Ruiz Fritis,Liceo Domingo Herrera Rivera,Sí,Sí,Sí,Más o menos,Más o menos,No,Sí,Más o menos,Sí
Belén Dubost Alfaro,Liceo Domingo Herrera Rivera,Sí,Más o menos,Sí,Sí,Más o menos,Más o menos,Sí,Sí,Sí
Daliha Orellana Humaña,Liceo Domingo Herrera Rivera,Sí,Más o menos,Sí,Más o menos,Sí,No,Sí,Sí,Sí
Juan Talamilla Jiménez,Liceo Domingo Herrera Rivera,Sí,Más o menos,Más o menos,No,Más o menos,Más o menos,Sí,Más o menos,Sí
Matías Gálvez Gaete,Liceo Domingo Herrera Rivera,Sí,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí
Máximo Díaz López,Liceo Domingo Herrera Rivera,Sí,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí
Sharon Guaitoto Duque,Liceo Domingo Herrera Rivera,Sí,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí,Sí
Thiago Cayuba Magueño,Liceo Domingo Herrera Rivera,Sí,Más o menos,Sí,Sí,Sí,Más o menos,Sí,Sí,Sí"""

with open("E:/dashboard_linea_azul/raw_desierto_azul_respuestas.csv", "w", encoding="utf-8") as f:
    f.write(desierto_azul_respuestas_raw)

with open("E:/dashboard_linea_azul/raw_desierto_azul_puntajes.csv", "w", encoding="utf-8") as f:
    f.write(desierto_azul_puntajes_raw)

with open("E:/dashboard_linea_azul/raw_climaton_respuestas.csv", "w", encoding="utf-8") as f:
    f.write(climaton_respuestas_raw)

print("Todas las tablas de Línea Azul guardadas con éxito.")
