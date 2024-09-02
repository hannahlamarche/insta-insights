import mongoose from 'mongoose';

const notFollowedSchema = new mongoose.Schema({
  username: String,
  full_name: String,
});

const IDontFollowBack = mongoose.model('IDontFollowBack', notFollowedSchema);

export { IDontFollowBack };