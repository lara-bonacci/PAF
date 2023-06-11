import Universe as uni
from Universe import AU

sun=uni.Planet("Sun",15,"y",1.989e30,(0.,0.),(0.,0.))
mercury=uni.Planet("Mercury",3,"slategrey",0.33010e24,(0.,0.4*AU),(47360.,0.))
venus=uni.Planet("Venus",5,"goldenrod",4.867e24,(0.,0.7*AU),(35020.,0.))
earth=uni.Planet("Earth",5,"g",5.9742e24,(0.,1.486e11),(29783.,0.))
mars=uni.Planet("Mars",4,"r",6.39e23,(0.,1.666*AU),(21970.,0.))


ss=uni.Universe(sun,mercury,venus,earth,mars)
ss.simulate(5*365*24*3600)