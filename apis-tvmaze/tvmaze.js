const missing_image = 'https://store-images.s-microsoft.com/image/apps.65316.13510798887490672.6e1ebb25-96c8-4504-b714-1f7cbca3c5ad.f9514a23-1eb8-4916-a18e-99b1a9817d15?mode=scale&q=90&h=300&w=300';

/** Given a query string, return array of matching shows:
 *     { id, name, summary, episodesUrl }
 */

/** Search Shows
 *    - given a search term, search for tv shows that
 *      match that query.  The function is async show it
 *       will be returning a promise.
 *
 *   - Returns an array of objects. Each object should include
 *     following show information:
 *    {
        id: <show id>,
        name: <show name>,
        summary: <show summary>,
        image: <an image from the show data, or a default imege if no image exists, (image isn't needed until later)>
      }
 */
async function searchShows(query) {
 
  // Get the results for shows using the query input.
  let results = await axios.get('http://api.tvmaze.com/search/shows', 
                                      {params: {q: `${query}`}});
  // Map only the specified info: id, name, summary, image.  
  let shows = results.data.map(result =>{
    let show = result.show;
    return {
      id: show.id,
      name: show.name,
      summary: show.summary,
      image: show.image  ? show.image.medium : missing_image
    }
  })
  // Return the new array with the mapped results. 
  return shows; 
}

/** Populate shows list:
 *     - given list of shows, add shows to DOM
 */
function populateShows(shows) {
  // Get the reference to the DOM that has an id of #shows-list. 
  const $showsList = $("#shows-list");
  $showsList.empty();

  // Populate the DOM with each show using a card. 
  for (let show of shows) {
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show"data-show-id="${show.id}">
        <div class="card" data-show-id="${show.id}">
          <img class="card-img-top" src="${show.image}">
          <div class="card-body">
            <h5 class="card-title">${show.name}</h5>
            <p class="card-text">${show.summary}</p>
            <button class="btn btn-primary">Episodes</button>
          </div>
        </div>
      </div>
      `);
    // Add to the DOM. 
    $showsList.append($item);
  }
}


/** Handle search form submission:
 *    - hide episodes area
 *    - get list of matching shows and show in shows list
 */

$("#search-form").on("submit", async function handleSearch (evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

  $("#episodes-area").hide();

  let shows = await searchShows(query);

  populateShows(shows);
});


/** Given a show ID, return list of episodes:
 *      { id, name, season, number }
 */
async function getEpisodes(id) {
  // Get the episodes list from the API. 
  let results = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`);
  // Map out the episode info: id, name, season, number.
  let episodes = results.data.map(episode =>{
    return{
      id: episode.id,
      name: episode.name,
      season: episode.season,
      number: episode.number
    }
  })
  // Return the new array with the mapped out info. 
  return episodes; 
}

// Populate the DOM with the episodes. 
function populateEpisodes(episodes){
  // Get the reference to the DOM that has an id of #episodes-list. 
  let $episodeListRef = $('#episodes-list'); 
  $episodeListRef.empty();

  // Create an li element and add the info for every episode. 
  for(let ep of episodes){
    let $item = $(`<li>${ep.name} (${ep.season}, number ${ep.number})</li>`);
    $episodeListRef.append($item);
  }
  // Show the episodes area, since default is hidden. 
  $('#episodes-area').show();
}

// A click event on episodes button to show a list of episodes. 
$('#shows-list').on('click', async e =>{
  // Get the ancestor of the card, which is '.Show' w/ data-attribute 'show-id'.
  let showID = $(e.target).closest('.Show').data('show-id');
  
  // Get the list of episodes using the showID of the card.
  let episodes = await getEpisodes(showID);
  populateEpisodes(episodes);
})