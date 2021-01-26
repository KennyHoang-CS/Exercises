const $searchInput = $('#search-term');
const $gifArea = $('#gif-area');

// A function to get a GIF to the GIF area. 
function addGIF(results){
    const length = results.data.length;

    // Get a random GIF out of the whole data-set. 
    let randomImageIndex = Math.floor(Math.random() * length);
    // Create a div container and place the GIF inside. 
    let $newDiv = $("<div>", {class: "col-md-4 col-12 mb-4"});
    let $newImg = $('<img>', {
            src: results.data[randomImageIndex].images.original.url,
            class: "w-100"
        });
    // Add to the gif area (output). 
    $newDiv.append($newImg);
    $gifArea.append($newDiv);
}

// A click event to add a GIF based on the search term. 
$('#submit').on('click', async function(e){
    e.preventDefault();

    // Get the search input and use it to get the specified results from GIPHY API. 
    try{
        let searchTerm = $searchInput.val();
        const results = await axios.get('http://api.giphy.com/v1/gifs/search',
                                    {params: {q: searchTerm, api_key: "dc6zaTOxFJmzC"}});
        addGIF(results.data);
    } catch(e){
        alert(e.name);
    }
})

// A function to remove all GIFs. 
$('#remove').on('click', ()=>{
    $gifArea.empty();
})