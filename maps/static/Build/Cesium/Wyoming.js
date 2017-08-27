var viewer = new Cesium.Viewer('cesiumContainer', {
    animation : true,
    timeline : true,
});

var wyoming = viewer.entities.add({
    name: 'Greenfields Seam',
    polygon: {
        hierarchy: Cesium.Cartesian3.fromDegreesArray([
            -109.080842, 45.002073,
            -105.91517, 45.002073,
            -104.058488, 44.996596,
            -104.053011, 43.002989,
            -104.053011, 41.003906,
            -105.728954, 40.998429,
            -107.919731, 41.003906,
            -109.04798, 40.998429,
            -111.047063, 40.998429,
            -111.047063, 42.000709,
            -111.047063, 44.476286,
            -111.05254, 45.002073]),
        height: 110,
        material: Cesium.Color.RED.withAlpha(0.5),
        outline: true,
        outlineColor: Cesium.Color.BLACK,

   }
});
wyoming.description =`<div><img src="static/images/30cfbee.jpg" style="width:25px;height:25px;border-radius:50%">Hey Ray! New data released!!! Check out the South corner!</div> <div><img src="static/images/30cfbee.jpg" style="width:25px;height:25px;border-radius:50%"><input type="text" placeholder="Enter Comment" style="width:290px;" />&nbsp;
<input type="submit" value="Add Comment" class="btn btn-primary" /></div>`
;
viewer.zoomTo(wyoming);
