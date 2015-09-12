// probably dont need disable geofences, as polygons are not used currently, 
var DISABLE_GEOFENCES = false;
var map;

var sightingData = new L.MarkerClusterGroup({
	maxClusterRadius: 100,
	polygonOptions: {
		color: '3B0B0B',
		weight: 3
	},
}).on('click', function(e) {
	var layer = e.layer;
	layer.bindPopup(getPopup(layer)).openPopup();
});


function initialize(scrollZoom) {
//	var accessToken = '{{ MAPBOX_ACCESS }}';
	L.mapbox.accessToken =  'pk.eyJ1IjoibWN0aG9tcHMiLCJhIjoidGNJUUVsVSJ9.U6CffdhpOp3l1i2CWPp5ag';
	//var mapboxID = '{{ MAPBOX_ID }}';	
	map = L.mapbox.map('map',  'mcthomps.km948apc')
							.setView([48.4222, -123.3657], 9)
							.addControl(L.mapbox.geocoderControl('mapbox.places'));
	var layer = L.geoJson();

	
	/*
	var featureLayer = L.mapbox.featureLayer()
	$.getJSON("{% url 'data' %}", function (data) {
		layer.addData(data);
	});
	map.addLayer(layer);
	*/
};

function geojsonMarker(data,type) {
	return L.geoJson(data, {
		pointToLayer: function(feature, latlng) {
			return L.marker(latlng, {
				icon: getIcon(type),
				ftype: type,
				objType: feature.properties.model
			})
		},
	});
};


var userLoc = L.mapbox.featureLayer().addTo(map);

function setView(lat, lng, zoom) {
	var marker;
		
	map.on("locationfound", function(location) {
		if(!marker)
			marker = L.userMarker(location.latlng, {smallIcon:true, circleOpts:{weight: 1, opacity: 0.3, fillOpacity: 0.05}}).addTo(map);
			marker.setLatLng(location.latlng);
			marker.setAccuracy(location.accuracy);
	});

	if (zoom) {
		this.map.setView(L.latlng(lat, lng), zoom);
		locateUser(setView = false, watch = false);
	} else {
		locateUser(setView = true, watch = false);
	}
};

function locateUser(setView, watch) {
	this.map.locate({
		setView: setView,
		maxZoom: 16,
		watch: watch,
		enableHighAccuracy: true
	});
};

