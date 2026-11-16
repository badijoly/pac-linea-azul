import csv
import json

# Script to save and parse all tables from Linea Azul

challwa_respuestas_raw = """Nombre,Colegio,Q1 PRE,Q2 PRE,Q3 PRE,Q4 especies PRE,Q5 razonamiento PRE,Q1 POST,Q2 POST,Q3 POST,Q4 especies POST,Q5 razonamiento POST
Alan Erazo Cuero,Escuela Claudio Matte Pérez,b,d,c,lobos marinos; mantarrayas,no habrian tiburones y no estarian en este ecosistema,b,b,b,mantarrayas; tiburones diferentes; pez guitarra; tiburon tollo fino,se moririan los peces y focas
Alonso Cárdenas Cabrera,Escuela Claudio Matte Pérez,d,d,c,peces; estrellas de mar,no se,d,b,d,pez,no se
Antonia Negrete Pastén,Escuela Claudio Matte Pérez,d,d,b,algas marinas; lobos marinos; peces,no se,b,b,b,peces,se secarian las microalgas y toda el agua se veria verde y fea
Ariana Morales Alpaca,Escuela Claudio Matte Pérez,d,d,c,peces; tiburones; medusas,no se que pasaria,d,b,c,pez; tiburon; ballena,desapareceran los animales marinos
Cristopher Padrón Cárdenas,Escuela Claudio Matte Pérez,d,d,d,peces; lobos marinos; leones marinos,no se,b,b,b,gatopardo; raya aguila; pez guitarra; pez gallo,muchas especies moririan
Janely Rodríguez Hernández,Escuela Claudio Matte Pérez,d,d,c,lobos marinos,no se,d,b,b,peces; lobos marinos,volverian las focas
José Arando Jiménez,Escuela Claudio Matte Pérez,d,b,d,no conozco ninguno,no se ninguno,d,c,b,no se,no hubiera comida
Luciana Urapiante Bilbao,Escuela Claudio Matte Pérez,d,d,c,lobos marinos; pescados,no se,b,b,b,pez; tiburon tollo; mantarraya aguila; pez zorro,los lobos marinos se duplicarian
Nahuel Prieto Campillay,Escuela Claudio Matte Pérez,a,b,c,peces; gaviotas; camarones,la gente se dara cuenta de que afecta la contaminacion,a,b,b,tiburones; rayas; ballenas; peces; lobos marinos,varias especies no se podrian reproducir
Ángel Vera Forero,Escuela Claudio Matte Pérez,d,d,c,medusas; peces/salmon; mariscos,"no se, nunca he ido alla",b,c,c,peces; medusas; algas,varios animales estarian en peligro de extincion
Alfonso Araos Torrejón,Escuela Ecológica Humberto González Echegoyen,b,b,a,chungungo; lobo marino; cabrilla; tomoyo; ajolote,afecta la alimentacion y la cadena,b,b,a,lobo marino; tiburones; ballenas; delfines; piures; peces locales; chorito,se complicaria la cadena alimenticia
Cristopher Salazar Medero,Escuela Ecológica Humberto González Echegoyen,a,d,c,mantarrayas; tiburones,no se,a,b,b,tiburones; mantas,los tiburones son esenciales: se comen a los lobos marinos y los lobos se comen los peces
Emilia Ahumada Araya,Escuela Ecológica Humberto González Echegoyen,d,d,d,tiburones; delfines; mantarrayas,afectaria en una cadena alimenticia,b,b,b,tiburones; delfines; ballenas; mantarrayas/rayas,afectaria porque se complicaria la cadena alimenticia
Javiera Paredes Jackson,Escuela Ecológica Humberto González Echegoyen,b,d,c,tiburones; peces; manta rayas,seria triste ya que se menciona mucho,b,b,d,tiburones; manta rayas; peces,habria mucha cantidad de especies
Kendra Calderón Viacava,Escuela Ecológica Humberto González Echegoyen,b,b,a,lobos marinos; chungungo; cabrilla,"el mundo depende de todos, afectaria la cadena alimenticia de la sociedad",b,b,no sabe,tiburon tollo manchado; tollo cazon; raya chilena,nos afectaria a nosotros y a los animales
Matias Roda Olivares,Escuela Ecológica Humberto González Echegoyen,b,b,b,tiburon martillo; leon marino/lobo marino; choritos; soles de mar,"sobrepoblacion de peces, mariscos y fauna nativa",b,b,b,tollo comun; leon marino; lobo marino,la sobrepoblacion de especies marinas
Maximiliano Cortés Barrios,Escuela Ecológica Humberto González Echegoyen,b,c,d,pez espada; lobo marino; leones marinos,afectaria la cadena alimenticia,b,c,d,lobo marino; leon marino,controlan las plagas
Máximo Alvarado Gordillo,Escuela Ecológica Humberto González Echegoyen,d,d,a,lobo marino; camella(?),afecta la cadena alimenticia,b,c,b,lobos marinos,la sobrepoblacion
Antonella Espinoza Manuelda,Escuela Ecológica Padre Alberto Hurtado,b,d,a,ballenas; peces; choritos; cangrejos,afectaria de alguna manera la cadena alimenticia,b,b,b,tiburon tollo; ballena azul; lobos marinos,"los lobos y focas se extinguirian y las algas aumentarian, haciendo el mar inhabitable"
María Paz Amira Valencia,Escuela Ecológica Padre Alberto Hurtado,b,d,c,lobos marinos; especies de peces; medusas,no sabria mucho sobre el tema ya que no sabia que habian,b,b,b,tiburon tollo; gato pardo; peje gallo (y mas de 60 especies),"el oceano cambiaria de color, habria mas algas y menos lobos marinos"
Roberto Ledezma Cuturrufo,Escuela Ecológica Padre Alberto Hurtado,d,d,c,tiburon blanco; mantarrayas,si desaparecieran podria afectar el mar,b,b,b,tiburon tollo; tiburon martillo,los focas revivirian extinguiendo la mayoria de animales marinos
Sofía Araos Bueno,Escuela Ecológica Padre Alberto Hurtado,b,c,b,lobos marinos; rayas,no se,b,b,b,tiburones; rayas,el agua se contaminaria y no hubiera sido habitable
Sofía Mella,Escuela Ecológica Padre Alberto Hurtado,b,a,c,peces; ballenas; tiburones; mantarrayas,no pasaria nada (confuso),b,a,c,tiburon tollo; pez; lobos,no habria algas
Álvaro Vargas,Escuela Ecológica Padre Alberto Hurtado,b,a,c,peces; medusas,,b,b,b,medusas; peces; tiburones,aumentaria la cantidad de peces
Aymeet Cueva Opazo,Escuela Javiera Carrera,b,d,d,lobo marino,no se,b,a,b,tiburon tollo; manta raya; tortugas,"no me acuerdo, pero los lobos marinos podrian morir mas"
Esteban Guerra Calle,Escuela Javiera Carrera,b,d,c,medusa; cangrejos; erizo de mar; estrella de mar,no se,b,b,b,tiburon tollo; medusas; tiburon martillo,el mar no serviria
Hugo Molina Naranjo,Escuela Javiera Carrera,a,d,c,tortuga; mantarraya; pez globo,no lo se pero lo voy a aprender,a,b,b,tiburon tollo; mantarrayas; tortugas,afectaria a nuestro planeta
León Chang Riveros,Escuela Javiera Carrera,b,b,a,tomo yo (sin respuesta valida),nada,a,b,b,toyo ajoa (ilegible),no se
Roben Díaz Condori,Escuela Javiera Carrera,d,b,d,lobos marinos; pez,no se,d,b,b,lobos marinos; pez,desapareceria los peces por los lobos
Sebastián Salazar Tapia,Escuela Javiera Carrera,b,a,c,tiburon blanco; reineta; pinguino de Humboldt; lobos marinos,los animales se saldrian de control,b,b,b,reineta; tiburon tollo; chungungo; pinguino de Humboldt,los peces se saldrian de control
Valery Cáceres Meneses,Escuela Javiera Carrera,d,d,c,lobos marinos; pez luna,no lo se pero me interesa saber,d,b,c,lobo marino; tollo comun,las focas se expandirian comiendo mas peces hasta que se extingan muriendo de hambre
Aliz Mollericona Ticona,Escuela Juan Pablo II,d,d,c,lobos marinos; ballenas; peces,ya no habria tiburones en Antofagasta,b,c,b,"tiburones (martillo, sierra); peces; lobos marinos",si ellos desaparecieran no podria comerse a los peces con enfermedades para proteger a los otros
Ana Campos,Escuela Juan Pablo II,d,d,b,no se,no se,d,b,b,muchos tiburones de distintos tamanos,habria un desbalance de todos los animales
Emilia Marín Castillo,Escuela Juan Pablo II,b,d,b,pez; pulpo; lobo marino,"nada, solo habrian pocas",b,c,b,pulpo; lobo marino,habria mucha poblacion de peces
Erik Serrano,Escuela Juan Pablo II,b,a,c,peces como el lenguado; las manoas,nada,b,a,b,tiburones; peces; manta raya,mal
Juan Sánchez Valencia,Escuela Juan Pablo II,b,b,d,delfin; tiburon tollo,,b,b,b,delfines; ballenas,no responde 
Mateo Torres Quispe,Escuela Juan Pablo II,b,d,a,peces; tiburones,no habria un depredador y el agua estara mas tranquila,b,b,b,tiburon tollo; peces; tiburon blanco; rayas,"los lobos marinos se reproducen mas, se comen todos los peces y no queda nada"
Nadriel Vaca Suárez,Escuela Juan Pablo II,b,d,d,focas; peces; ballenas en invierno,no habria muchos tiburones / no se,b,c,b,tiburones; mantas; rayas; focas; ballenas; peces,se hubiese alimento para algunos animales
Patricio Chandía González,Escuela Juan Pablo II,b,a,b,ballenas,posiblemente se extingan,b,c,b,diferentes tipos de tiburones; ballenas,seria muy malo porque son una especie muy importante
Aron Ardiles Vega,Escuela República de Estados Unidos,b,d,c,lobos marinos; ballenas; pinguinos,no se porque no ha pasado,b,b,b,lobo marino; tiburon tollo,que el agua se pone muy caliente
Aylynn Opazo Carvajal,Escuela República de Estados Unidos,b,d,c,lobos marinos; ballenas; pinguinos de Humboldt,no se,b,a,b,lobos marinos; ballenas; pinguinos de Humboldt,habria sobrepoblacion de peces y los lobos marinos se comen los peces y los peces desapareceran
Berenice Jora Zarate,Escuela República de Estados Unidos,d,d,d,no se,no habria canibalismo,b,b,d,no se,no se
Evelyn Estigarribia Choquecota,Escuela República de Estados Unidos,b,d,c,lobos marinos; focas; tiburones,se extinguirian,b,b,c,tiburones; mantarrayas; lobos marinos; focas,habrian muchas mas bacterias
Jorge Seas Tomicha,Escuela República de Estados Unidos,b,c,c,lobo marino; ballena,"podria pasar cualquier cosa, como a la gente, no se",b,c,c,tiburon ballena; pez,"pasaria que ya saldrian de la playa o podria comerse a la gente, no se"
Keyla Morán González,Escuela República de Estados Unidos,b,d,b,lobo marino; pinguino de Humboldt; ballenas,no se tema,b,b,b,lobo marino; pinguinos; tiburon tollo,habria un desequilibrio total en los mares
Lucas Llanqui Honorio,Escuela República de Estados Unidos,b,d,c,peces; rayas; algas; lobos marinos; ballenas,la fauna marina aumentaria,b,b,b,lobos marinos; tiburones tollos,hubiera sobrepoblacion de peces
Matías Orellana Flores,Escuela República de Estados Unidos,b,d,c,pinguino de Humboldt; lobos marinos; ballenas,creo que afecta la cadena alimenticia pero en si no se,b,b,b,lobo marino; tiburon tollo fino; manta raya; gatopardo; tiburon tollo comun; tiburon ballena; rayas,cambiaria el mar para mal
Minzy Díaz Vergara,Escuela República de Estados Unidos,b,d,c,lobos marinos; pinguinos de Humboldt; ballenas,no se sobre el tema,b,b,b,lobo marino; pinguinos; tiburones (6 especies),el equilibrio seria muy evidente ya que son muy importantes en la vida
Ariatna Herrera Caicedo,Escuela República de Italia,b,b,b,pescado; tiburones; rayas,"no se, pero creo que no hubiera sobrepesca",b,c,b,tiburon/ballena; mantas; lobos,desaparecerian lobos marinos y tiburones y hubiera contaminacion
Arshiel Gronchi Martínez,Escuela República de Italia,b,c,c,tiburon ballena; lobos marinos,"dejaria de ser tan peligroso, ya no estariamos en un lugar tan peligroso",b,b,b,tiburon tollo; lobos marinos,"bajaria el tema de la pesca, no correriamos riesgo"
Emilia Narváez Narváez,Escuela República de Italia,b,c,b,(tachado),no podriamos vivir,b,c,a,no se,no se
Fernando Aros Santus,Escuela República de Italia,b,d,c,peces pequenos; pez globo; pez lobo; estrellas de mar; erizos; tiburon,creo que los peces se reproducen mas rapido y no hay peces muertos,b,b,b,peces pequenos; pez loro; tiburon tollo; manta raya; raya de profundidad,"las focas se comerian los peces, el mar seria una sopa y todos moririamos"
Jesús Rivero Velásquez,Escuela República de Italia,a,d,a,lobo marino,no se,a,b,b,lobo marino,hubiese una sobrepoblacion de lobos marinos
José Rivero Velásquez,Escuela República de Italia,d,d,d,pez; lobos marinos; tiburones,no se,c,b,b,tiburones; mantarrayas,habria una sobrepoblacion
Kiara Carvajal Mondaca,Escuela República de Italia,a,b,c,tiburon; peces,no se,c,b,c,tiburones; peces,no se
María Rementería Ardiles,Escuela República de Italia,b,d,a,tiburon ballena (pero nunca he escuchado tiburones),no habria mas muertes y nada mas,b,a,a,pez electrico,no habria comida ni oxigeno
Nicol Palacios Cruz,Escuela República de Italia,b,d,b,pescados; rayas; tiburones,no podrian vivir a causa de la sobrepesca,b,c,b,tiburon ballena; raya aguila chilena,puede cambiar todo un habitat
Thais Opazo Ovando,Escuela República de Italia,d,c,a,pescados; lobo marino; delfines,no se,d,c,c,peces; lobos marinos; delfines,no se
Antonella Ruiz Fritis,Liceo Domingo Herrera Rivera,d,d,b,lobos marinos; lapas; caracoles marinos,no se,d,b,b,tiburon tollo; lobo marino; lapa,todo el mar estaria muy lleno de peces
Belén Dubost Alfaro,Liceo Domingo Herrera Rivera,b,a,b,caracoles de mar; chanchitos de mar; peces; pulpos,no se,b,b,b,chanchitos de mar,no nos va oxigeno
Daliha Orellana Humaña,Liceo Domingo Herrera Rivera,d,d,b,lobo marino; estrella marina; erizo de mar; foca; tiburones; orca; pinguinos; delfines,no lo se,d,b,b,foca; tiburon; peces,cambiarian varios factores del mar
Ignacia Reyes Yau,Liceo Domingo Herrera Rivera,d,d,d,ballenas; peces; caracoles marinos; pulpos,no lo se,d,d,d,ballena; caracol; pulpo,el agua se contaminara mas
Juan Talamilla Jiménez,Liceo Domingo Herrera Rivera,b,c,b,tiburon ballena; lobo marino; peces,no lo se pero algo grave probablemente,b,b,b,tiburon tollo/nazla; tiburon martillo; tiburon ballena; tiburon pejegallo,los lobos marinos creceran en cantidad grande y como no podran alimentarse moririan
Matías Gálvez Gaete,Liceo Domingo Herrera Rivera,d,b,b,no se,no se,b,b,b,tiburon martillo; tiburon tollo,no se
Máximo Díaz López,Liceo Domingo Herrera Rivera,d,d,d,medusas,mal,d,d,d,no se,no se
Sharon Guaitoto Duque,Liceo Domingo Herrera Rivera,b,a,c,caballitos de mar; cangrejos; pulpos; pescados; camarones; chanchitos de mar,alteraria la fauna marina en Antofagasta,b,b,b,mantarraya; tiburon tollo; angelote,nos quedamos sin oxigeno
Thiago Cayuba Magueño,Liceo Domingo Herrera Rivera,d,b,d,ballenas,no se,b,b,b,tiburon; tollo,habria restos de animales y ellos nos alimentan en el mar y el oxigeno"""

with open("E:/dashboard_linea_azul/raw_challwa_respuestas.csv", "w", encoding="utf-8") as f:
    f.write(challwa_respuestas_raw)

print("Challwa respuestas guardadas")
