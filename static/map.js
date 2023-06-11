var map = L.map('map').setView([0, 0], 2);
    L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2', 'mt3'],
        noWrap: true,
    }).addTo(map);
    var userProfiles = JSON.parse('{{ user_profiles_json|escapejs }}');
    userProfiles.forEach(function (userProfile) {
        var marker = L.marker([userProfile.latitude, userProfile.longitude]).addTo(map);
        var popupContent = `
                <div>
                    <h3>${userProfile.user__first_name} ${userProfile.user__first_name}</h3>
                    <p>Email: ${userProfile.user__email}</p>
                    <p>Home Address: ${userProfile.home_address}</p>
                    <p>Phone Number: ${userProfile.phone_number}</p>
                </div>
            `;
            marker.bindPopup(popupContent);
        });
        
        map.on('popupopen', function(event) {
            var marker = event.popup._source;
            marker.setOpacity(0.7);
        });
        
        map.on('click', function(event) {
            map.closePopup();
    });