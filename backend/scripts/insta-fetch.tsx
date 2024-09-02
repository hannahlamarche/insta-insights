import axios from 'axios';


const username = "lola_the_cow_";

let followers = [{ username: "", full_name: "" }];
let followings = [{ username: "", full_name: "" }];
let dontFollowMeBack = [{ username: "", full_name: "" }];
let iDontFollowBack = [{ username: "", full_name: "" }];

followers = [];
followings = [];
dontFollowMeBack = [];
iDontFollowBack = [];

(async () => {
  try {
    // Your existing Instagram script logic...

    // After processing the data, send it to your Express backend
    await axios.post('http://localhost:5000/save-instagram-data', {
      followers,
      followings,
      dontFollowMeBack,
      iDontFollowBack,
    });

    console.log('Data sent to the backend!');
  } catch (err) {
    console.log({ err });
  }
})();
