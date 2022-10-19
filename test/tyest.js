//hacer una funcion que traiga un api de pokemon y que me traiga el nombre y la imagen

const fetch = require('node-fetch')

const getPokemon = async (id) => {
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
  const data = await response.json()
  const pokemon = {
    name: data.name,
    image: data.sprites.front_default
  }
  return pokemon
}

getPokemon(1).then(pokemon => {
  console.log(pokemon)
})
