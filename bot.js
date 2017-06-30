console.log("bot is online");

var Twit = require('twit');
var config = require('./config');
var T = new Twit(config);
var stream = T.stream('user');

stream.on('follow', followed);
function followed(eventFollow) {

  var name = eventFollow.source.name;
  var screenName  = eventFollow.source.screen_name;
  tweetIt('@' + screenName  + ' ' + 'did you get the message');
}

stream.on('tweet', tweetEvent);
function tweetEvent(eventMsg){

  var replyto = eventMsg.in_reply_to_screen_name;
  var text = eventMsg.text;
  var from = eventMsg.user.screen_name;

  console.log(replyto + ' ' + from);

  if(replyto === 'Coffe_Pot_slave'){

    var newTweet = '@' + from + 'buidling';
    tweetIt(newTweet);
  }
}
function tweetIt(txt){

  var tweet =  {
       status: txt
      }

      T.post('statuses/update', tweet, tweeted);

      function tweeted (err, data, response) {
        if (err){
          console.log("something went wrong");
        }
        else{
          console.log("working like a charm");
        }
      }
}
