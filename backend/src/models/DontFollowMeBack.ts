import mongoose from 'mongoose';

const notFollowedSchema = new mongoose.Schema({
  username: String,
  full_name: String,
});

const DontFollowMeBack = mongoose.model('DontFollowMeBack', notFollowedSchema);

export { DontFollowMeBack };