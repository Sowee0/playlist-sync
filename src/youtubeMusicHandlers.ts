import config from "../config.json";
import * as ytMusic from "node-youtube-music";

export const findSong = async (songQuery: string) => {
  const songs = await ytMusic.searchMusics(songQuery);

  if (songs && songs[0] && songs[0].youtubeId) {
    console.log("songs", songs[0]);
  }
};

export const getPlaylist = async (playlistId: string) => {
  const playlist = await ytMusic.listMusicsFromPlaylist(playlistId);
};

export const ytmAddSong = async (videoId: string) => {
  await fetch(
    "https://music.youtube.com/youtubei/v1/browse/edit_playlist?key=AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30&prettyPrint=false",
    {
      credentials: "include",
      headers: {
        "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        Accept: "*/*",
        "X-Goog-AuthUser": "0",
        "X-Origin": "https://music.youtube.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "same-origin",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        Authorization: config.YTM_TOKEN_1,
        "Alt-Used": "music.youtube.com",
        Pragma: "no-cache",
        "Cache-Control": "no-cache",
      },
      referrer:
        "https://music.youtube.com/browse/VLPLKPa_-QZ5p9Xh9eqwR1op3YCpmJCXhdC1",
      body: '{"context":{"client":{"hl":"en","gl":"BR","remoteHost":"2804:14c:fc81:880e:d41e:ede7:29bd:444e","deviceMake":"","deviceModel":"","visitorData":"CgtmWTlWeTNXdEdGRSjX0d2ZBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0,gzip(gfe)","clientName":"WEB_REMIX","clientVersion":"1.20220926.01.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://music.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CNfR3ZkGEODNrgUQrMyuBRD9uP0SEMvs_RIQ1IOuBRDbyq4FELfLrQUQvs2uBRCZxq4FELiLrgUQlM-uBRDqyq4FEM2F_hIQ4rmuBRDYvq0F"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"America/Sao_Paulo","browserName":"Firefox","browserVersion":"106.0","screenWidthPoints":1369,"screenHeightPoints":893,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":-180,"musicAppInfo":{"pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_UNKNOWN","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","storeDigitalGoodsApiSupportStatus":{"playStoreDigitalGoodsApiSupportStatus":"DIGITAL_GOODS_API_SUPPORT_STATUS_UNSUPPORTED"},"musicActivityMasterSwitch":"MUSIC_ACTIVITY_MASTER_SWITCH_INDETERMINATE","musicLocationMasterSwitch":"MUSIC_LOCATION_MASTER_SWITCH_INDETERMINATE"}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clientScreenNonce":"MC42NDU3NTE3NDE1NDUyNDgx","clickTracking":{"clickTrackingParams":"CFIQ9p4FIhMIl_nAzsa9-gIVY05IAB3qiQAP"},"adSignalsInfo":{"params":[{"key":"dt","value":"1664575704227"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-180"},{"key":"u_his","value":"2"},{"key":"u_h","value":"900"},{"key":"u_w","value":"1440"},{"key":"u_ah","value":"900"},{"key":"u_aw","value":"1440"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"893"},{"key":"biw","value":"1352"},{"key":"brdim","value":"521,0,521,0,1440,0,1369,893,1369,893"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]},"activePlayers":[{"playerContextParams":"Q0FFU0FnZ0I="}]},"actions":[{"addedVideoId":"U6PSsSM1swQ","action":"ACTION_ADD_VIDEO"}],"params":"IAEwAQ%3D%3D","playlistId":"PLKPa_-QZ5p9Xh9eqwR1op3YCpmJCXhdC1"}',
      method: "POST",
      mode: "cors",
    }
  );
};
