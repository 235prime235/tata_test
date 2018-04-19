import os

def view_colors():

    template_header_file = os.getcwd() + "/templates/header.html"
    template_navbar_file = os.getcwd() + "/templates/colors_navbar.html"
    template_footer_file = os.getcwd() + "/templates/footer.html"

    with open (template_header_file, "r") as navfile:
        str_header = navfile.read()
    
    with open (template_navbar_file, "r") as navfile:
        str_navbar = navfile.read()

    with open (template_footer_file, "r") as navfile:
        str_footer = navfile.read()

##HEADER
    str_page = str_header
    str_page = str_page + str_navbar

##BODY
    str_page = str_page + """
    
<body>
    <div class="site-container">
        <div id="canvas" style="float:right">
            
            <script src="/static/js/three.js"></script>
            <script src="/static/js/OrbitControls.js"></script>
            <script src="/static/js/TDSLoader.js"></script>

            <script>
            
            var scene = new THREE.Scene();
            var renderer = new THREE.WebGLRenderer();
            renderer.setClearColor( 0xeeeeee, 1);
            var container = document.getElementById('canvas');
            var w = container.offsetWidth;
            var h = container.offsetHeight;
            renderer.setSize(w, h);
            var camera = new THREE.PerspectiveCamera( 75, w/h, 0.1, 1000 );
            container.appendChild(renderer.domElement);

            var orbit = new THREE.OrbitControls( camera, renderer.domElement );
            orbit.enableZoom = true;

            var lights = [];
            lights[ 0 ] = new THREE.PointLight( 0xffffff, 1, 0 );
            lights[ 1 ] = new THREE.PointLight( 0xffffff, 1, 0 );
            lights[ 2 ] = new THREE.PointLight( 0xffffff, 1, 0 );

            lights[ 0 ].position.set( 0, 200, 0 );
            lights[ 1 ].position.set( 100, 200, 100 );
            lights[ 2 ].position.set( - 100, - 200, - 100 );

            scene.add( lights[ 0 ] );
            scene.add( lights[ 1 ] );
            scene.add( lights[ 2 ] );

            

            var color = new THREE.Color("rgb(255, 0, 0)");
            
            
            function AddFlat(){

                scene.remove(scene.children[3]);

                var geometry = new THREE.BoxGeometry( 1, 1, 1 );
                var material = new THREE.MeshPhongMaterial( {
                    color,
                    emissive: 0x072534,
                    side: THREE.DoubleSide,
                    flatShading: true } );
                
                var cube = new THREE.Mesh( geometry, material );
                scene.add( cube );

                camera.position.x = 0;
                camera.position.y = 0;
                camera.position.z = 5;

                var animate = function () {
                    requestAnimationFrame( animate );

                    

                    renderer.render(scene, camera);
                    };

                animate();

            }


            function AddBox(){

                scene.remove(scene.children[3]);
            
                var geometry = new THREE.BoxGeometry( 3, 3, 3 );
                var material = new THREE.MeshPhongMaterial( {
                    color,
                    emissive: 0x072534,
                    side: THREE.DoubleSide,
                    flatShading: true } );
                
                var cube = new THREE.Mesh( geometry, material );
                scene.add( cube );

                camera.position.x = 0;
                camera.position.y = 0;
                camera.position.z = 5;

                var animate = function () {
                    requestAnimationFrame( animate );

                    

                    renderer.render(scene, camera);
                    };

                animate();

            }


            function AddPanel(){

                scene.remove(scene.children[3]);
            
                var loader = new THREE.TDSLoader( );
				
				loader.load( '/static/models/panel.3ds', function ( object ) {
					object.traverse( function ( child ) {
						
					} );
					
                    
                    object.scale.set(0.003, 0.003, 0.003)
                    scene.add( object );

                });

                camera.position.x = 0;
                camera.position.y = 0;
                camera.position.z = 5;

                
            var animate = function () {
                    requestAnimationFrame( animate );

                    

                    renderer.render(scene, camera);
                    };

                animate();
                  

            }


            function AddBuilding(){

                scene.remove(scene.children[3]);
            
                var loader = new THREE.TDSLoader( );
				
				loader.load( '/static/models/building.3ds', function ( object ) {
					object.traverse( function ( child ) {
						
					} );
					
                    
                    object.scale.set(0.003, 0.003, 0.003)
                    scene.add( object );

                });

                camera.position.x = 0;
                camera.position.y = 0;
                camera.position.z = 120;

                
            var animate = function () {
                    requestAnimationFrame( animate );

                    

                    renderer.render(scene, camera);
                    };

                animate();

            }

            AddFlat();

            </script>

        
	<div class="btn-group" style="float:left">
		<button class="button" onclick="AddBuilding()">Wall</button>
  		<button class="button" onclick="AddPanel()">Panel</button>
  		<button class="button" onclick="AddBox()">3d</button>
  		<button class="button" onclick="AddFlat()">Flat</button>
	</div>
</div>
</div>



</body>
    """

##FOOTER
    str_page = str_page + str_footer

    return str_page