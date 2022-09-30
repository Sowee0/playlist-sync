import express from "express";
import config from "./config.json";

import { findSong, getPlaylist } from "./src/youtubeMusicHandlers";

findSong("Major Crimes Health & Window Weather");

getPlaylist("PLKPa_-QZ5p9Xh9eqwR1op3YCpmJCXhdC1");
