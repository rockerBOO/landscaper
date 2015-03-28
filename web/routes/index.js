var express = require('express');
var router = express.Router()

var _ = require('underscore')

var elasticsearch = require('elasticsearch');
var client = new elasticsearch.Client({
  host: 'localhost:9200',
  log: [{
	  type: 'stdio',
	  levels: ['error', 'warning']
	}]
});
	
var flickr = require('flickrapi'),
		flickrOptions =  {
    api_key: "88c471e464bc615fd2b969136ef4315a",
    secret: "f3498350521a543b",
    progress: false
}

flickr.tokenOnly(flickrOptions, function(error, flickr) {
  // we can now use "flickr" as our API object,
  // but we can only call public methods and access public data
  		flickr.photos.search({
			  page: 1,
			  per_page: 10,
			  text: 'Quercus alba',
			  sort: 'interestingness-desc',
			  license: '1,2,3,4,5,6,7,8',
			}, function(err, result) {
				if (err) 
					return console.log(err)


				console.log(result)
			  // result is Flickr's response
			  //console.log('flicka', result.photos.photo)

			  result.photos.photo.forEach(function(e) {
			  		// "https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg"
			  		url = "https://farm"+e.farm+".staticflickr.com/"+e.server+"/"+e.id+"_"+e.secret+".jpg"
			  		console.log(url)
			  });
			});
});

/* GET home page. */
router.get('/', function(req, res, next) {
  var input = {
  	name: req.query.name,
  	sname: req.query.sname,
  	sun: req.query.sun,
  	water: req.query.water,
  	habit: req.query.habit
  }

  var must = []

 	_.each(req.query, function (element, index) {
 		if (false == element || typeof element == 'string') {
 			return;
 		}

 		var index = index

 		element.forEach(function(e) {
 			x = {match: {}}

	 		x.match[index.capitalize()] = e

	 		must.push(x);
 		});
 	});

 	console.log('must', must)

	client.search({
	  index: 'landscaper',
	  type: 'wildflowerorg',
	  body: {
	    query: {
				"bool": {
			  	"must": must
			  }
		  }
	  },
	  size: 100
	}).then(function (resp) {
	    var hits = resp.hits.hits;

	  // console.log(resp)

    var meta = {
     	total: resp.hits.total,
     	max_score: resp.hits.max_score
    }

    console.log(resp)

	    var plants = [] 

	    hits.forEach(function(element, index) {


	    /*
			flickr.photos.search({
			  user_id: flickr.options.user_id,
			  page: 1,
			  per_page: 500
			}, function(err, result) {
			  // result is Flickr's response
			  console.log(result)
			});
			*/

	    	plants.push({
	    		names: element['_source']['Common Name'], 
	    		snames: element['_source']['Scientific Name'],
	    		habit: element['_source']['Habit'],
	    		sun: element['_source']['Sun'],
	    		duration: element['_source']['Duration'],
	    		water: element['_source']['Water'],
	    		score: element['_score'],
	    		type: element['_type'],
	    		index: element['_index']
	    	})
	    });

	    res.render('index', { 
	    	page_title: 'Plant Lister',
	    	plants: plants, 
	    	input: input, 
	    	'_': _,
	    	meta: meta, 
	    });
	}, function (err) {
	    console.trace(err.message);
	});


  
});

String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

module.exports = router;
