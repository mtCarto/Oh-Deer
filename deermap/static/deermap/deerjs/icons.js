var AnimalIcon = L.Icon.extend({
	options: {
		iconSize: [32, 37],
		iconAnchor: [16, 0],
		popupAnchor: [-5, -10]
	}
});

var deerIcon = new AnimalIcon({iconUrl: '/static/deermap/data/images/icons/deer.png'}),
		hareIcon = new AnimalIcon({iconUrl: '/static/deermap/data/images/icons/hare.png'}),
		rodentIcon = new AnimalIcon({iconUrl: '/static/deermap/data/images/icons/rodent.png'}),
		pawIcon = new AnimalIcon({iconUrl: '/static/deermap/data/images/icons/paw.png' });

//given type, return icon
function getIcon(t) {
	if ( t === "deer")
		return icons["deerIcon"];
	else if (t === "hare")
		return icons["hareIcon"];
	else if (t === "rodent")
		return icons["rodentIcon"];
	else if (t === "paw")
		return icons["pawIcon"];
	else 
		return;
};
