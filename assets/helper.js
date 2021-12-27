function send_analytics(post_header){
    fetch('https://www.probhakarsarkar.com/analytics/registerevent', {
  method: 'post',
  headers: {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
	"event_type": "nontech_blog_click",
	"link": post_header
    })
    }).then(res => res.json())
      .then(res => console.log(res));
}