from Modelos import *

#Generar modelo Gn,m de Erdös y Rényi
#g = grafo_ErdosRenyi(50,60)
#g.mostrar_grafo()
#g.exportar_a_gv("Erdos_500.gv")
#g.dijkstra(5)
#g.exportar_dijkstra_gv(5,'Erdos_Dijkstra_30.gv')



#Generar modelo Gn,p de Gilbert
#g = grafo_Gilbert(50,6)
#g.mostrar_grafo()
#g.exportar_a_gv("Gilbert300.gv")



#Generar modelo Gn Dorogovtsev-Mendes
#g = grafo_DoroMendes(50)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_DoroMendes_500.gv")



#Generar modelo Gm,n de malla
#g = grafo_Malla(8,5)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_Malla_25.gv")
#g = grafo_Geografico(500,0.2)

#Generar variante del modelo Gn,d Barabási-Albert
#g = grafo_BarabasiAlbert(50,5)
#g.mostrar_grafo()
#g.exportar_a_gv("Grafo_Barabasi_20.gv")

#nodo_inicial = g.nodos[0]

# Ejecutar Dijkstra
#arbol, dist, padres = g.dijkstra(nodo_inicial)

# Exportar el camino más corto de inicio a fin
#g.exportar_dijkstra_gv("Dijkstra_Geografico_50.gv", nodo_inicial, padres)


#g.exportar_a_gv1("KruskalI_Erdos30.gv","Kruskal inverso", mst)
#mst.exportar_a_gv("Prim_Erdos50.gv")


#costo_mst, aristas_mst = g.kruskalD()
#g.exportar_mst_gv('Kruskal_prueba.gv', aristas_mst)



#print("Costo total MST:", costo_mst)
#print("Aristas en MST:")
#for arista in aristas_mst:
#    print(f"{arista.origen} -- {arista.destino} : peso={arista.peso}")

#Generar modelo Gn,r geográfico simple
g = grafo_Geografico(50,0.5)
#g.mostrar_grafo()
kruskalinv = g.KruskalI()
g.exportar_mst_a_gv(kruskalinv, "KruskalI_Geografico50.gv")
#g.exportar_a_gv("Grafo_Geografico_400.gv")
#
# g.BFS(10)
#g.exportar_a_gv_algoritmo("Grafo_Geografico_BFS_500.gv")
#arbol_dfs = g.DFS_recursiva(40)
#g.exportar_arbol_dfs_a_gv(arbol_dfs,"Geografico_dfsR_500.gv")
#arbol_dfs_i = g.DFS_iterativa(10)
#g.exportar_arbol_dfs_a_gv(arbol_dfs_i, "Geografico_DFS_I_500.gv")




