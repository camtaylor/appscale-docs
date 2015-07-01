 $(document).ready(function(){
         var appscaleUp = 'Starting AppScale 2.3.1 over a virtualized cluster. \n' +
                          'Log in to your head node: ssh -i /Users/you/.appscale/appscale.key root@192.168.33.10 \n'+
                          'Head node successfully initialized at 192.168.33.10. It is now starting up cassandra. \n'+
                          'Copying over deployment credentials \n' +
                          'Starting AppController at 192.168.33.10 \n' +
                          'Please wait for the AppController to finish pre-processing tasks. \n';
         var ls = "AppScalefile  guestbook";
         var appscaleDeploy = "This AppScale instance is linked to an e-mail address giving it administrator privileges. \n" +
                              "... \n" +
                              "Done starting up AppScale, now in heartbeat mode \n" +
                              "\n" +
                              "Uploading guestbook... \n" +
                              "We have reserved the name guestbook for your application. \n" +
                              "Creating remote directory to copy app into \n" +
                              "Updating AppController \n" +
                              "Please wait for your app to start up. \n" +
                              " \n" +
                              "Your app can be reached at the following URL: http://192.168.33.10:8080 \n";
         /* Fifth console */
         var console5 = $('<div class="console1">');
         $('#content-column').append(console5);
         var controller5  = console5.console({
          promptLabel: 'AppScale > ',
          commandHandle:function(line){

            // switch statement to parse command line input
            switch(line) {
              case "appscale up":
                $("#nextButton").toggleClass("btn-primary btn-success");
                $("#title").fadeOut("slow");
                $("#title").hide().html('Appscale is now up and running.').fadeIn("slow");
                return [{msg: appscaleUp,className:"jquery-console-message-value"}];
                break;
              case "appscale down":
                $("#title").fadeOut("slow");
                $("#title").hide().html('Appscale is now down.').fadeIn("slow");
                break;
              case "ls":
                $("#title").fadeOut("slow");
                $("#title").hide().html('You can see the example application and the AppScalefile. Try typing appscale deploy guestbook').fadeIn("slow");
                return [{msg: ls,className:"jquery-console-message-value"}];
                break;
              case "appscale deploy guestbook":
                $("#title").fadeOut("slow");
                $("#title").hide().html('The guestbook application is now deployed').fadeIn("slow");
                return [{msg: appscaleDeploy,className:"jquery-console-message-value"}];
                break;
              default:
                var m = "Unrecognized command \'" + line + "\'";
                return [{msg: m,className:"jquery-console-message-value"}];
            }
           
          },
          colors: ["red","blue","green","black","yellow","white","grey"],
          cols: 40,
          completeHandle:function(prefix){
            var colors = this.colors;
            var ret = [];
            for (var i=0;i<colors.length;i++) {
              var color=colors[i];
              if (color.lastIndexOf(prefix,0) === 0) {
                ret.push(color.substring(prefix.length));
              }
            }
            return ret;
          }
         });
      });