part_a = '''
<!DOCTYPE html>
<html>
<head>
<style>
#tweeters {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#tweeters td, #tweeters th {
  border: 1px solid #ddd;
  padding: 8px;
}

#tweeters tr:nth-child(even){background-color: #f2f2f2;}

#tweeters tr:hover {background-color: #ddd;}

#tweeters th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Top Tweeters for Conference 2023</h1>

<table id="tweeters">
  <thead>
    <tr>
      <th>User</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody id="data">

'''

part_b = '''
  </tbody>
</table>
</body>
</html>

'''