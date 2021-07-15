"""Main py"""

from world.var.inputs import create_var, create_par, variables
from world.create_worlds import universe, world_creator, prob_get
from world.worlds_class import build_var_names

create_var()
create_par()


for i in variables:
    i.build_prob()
    print(i.prob)
    print(i.getprob)


build_var_names()
world_creator()
prob_get()
for i in universe:
    print(i.world)
    i.build_world_prob()
    print(i.p_world)
    print(i.prob)
