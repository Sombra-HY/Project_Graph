from simples import vef_simples
# COMPLETO
#
# Para ser completo o quantidade de vertices -1 tem que ser igual
# ao soma de elemento da linha,
#  [0,1,1] = 3 -1 =2 == sum(0,1,1)
#  [1,0,1] = 3 -1 =2 == sum(1,0,1)
#  [1,1,0] = 3 -1 =2 == sum(1,1,0)

def completo(m):
    var = 0

    if vef_simples(m)[0]==True:
        var = 1

        for x in m:
            if sum(x) != (len(x)-1):
                var = 0

    return True if var==1 else False
