<head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-31952622-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Plurk OAuth API',
    'author': 'Cheng-Lung Sung',
    'url': 'https://github.com/clsung/plurk-oauth',
    'download_url': 'http://pypi.python.org/pypi/plurk-oauth',
    'author_email': 'clsung@gmail.com',
    'version': '0.5.0',
    'install_requires': ['nose', 'oauth2'],
    'packages': ['plurk_oauth'],
    'scripts': ['bin/get_own_profile.py', 'bin/post_to_plurk.py'],
    'name': 'plurk-oauth'
}

setup(**config)
