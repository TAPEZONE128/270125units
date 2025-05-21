# Programming Languages

## PHP 

A quick reference for embedding and writing PHP code inside HTML.

---

## Basic Syntax

```php
<?php
  // PHP code goes here
  echo "Hello, World!";
?>
```

## Short Echo Tag (for output only)
```php
<?= "This is a short echo tag."; ?>
```

## Embedding PHP in HTML
```php
<!DOCTYPE html>
<html>
<head>
  <title>PHP in HTML</title>
</head>
<body>

<h1><?php echo "Welcome to my site!"; ?></h1>

<p>The year is <?= date("Y"); ?></p>

</body>
</html>
```

## PHP Control Structures in HTML

### If / Else
```php
<?php $loggedIn = true; ?>

<?php if ($loggedIn): ?>
  <p>Welcome back, user!</p>
<?php else: ?>
  <p>Please log in.</p>
<?php endif; ?>
```

### Loop (foreach)
```php
<?php $colors = ["Red", "Green", "Blue"]; ?>

<ul>
  <?php foreach ($colors as $color): ?>
    <li><?= $color; ?></li>
  <?php endforeach; ?>
</ul>
```

## Forms and PHP

### HTML Form
```html
<form method="post" action="process.php">
  <input type="text" name="username" placeholder="Enter name">
  <input type="submit" value="Submit">
</form>
```

### Processing Form in PHP
```php
<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["username"]);
    echo "Hello, " . $name;
  }
?>
```

## PHP Variables and Data Types
```php
<?php
  $string = "Hello";
  $int = 42;
  $float = 3.14;
  $bool = true;
  $array = [1, 2, 3];
  $assoc = ["name" => "John", "age" => 30];
?>
```

## Including Files
```php
<?php include 'header.php'; ?>
<?php require 'config.php'; ?>
```
`include` will only show a warning on failure.
`require` will cause a fatal error on failure.

## PHP Functions

```php
<?php
  function greet($name) {
    return "Hello, $name!";
  }

  echo greet("Alice");
?>
```

## File Handling
```php
<?php
  $file = fopen("data.txt", "r");
  while (!feof($file)) {
    echo fgets($file) . "<br>";
  }
  fclose($file);
?>
```

## Superglobals
| Variable    | Description                        |
| ----------- | ---------------------------------- |
| `$_GET`     | Data from URL query string         |
| `$_POST`    | Data from form (POST method)       |
| `$_SERVER`  | Server info (headers, paths, etc.) |
| `$_SESSION` | Session variables                  |
| `$_COOKIE`  | Cookies sent by the browser        |
| `$_FILES`   | Uploaded files via form            |
| `$_ENV`     | Environment variables              |

## Useful Functions
| Function             | Use                            |
| -------------------- | ------------------------------ |
| `htmlspecialchars()` | Escape HTML special characters |
| `isset()`            | Checks if a variable is set    |
| `empty()`            | Checks if a variable is empty  |
| `strtoupper()`       | Converts to uppercase          |
| `explode()`          | Split string into array        |
| `implode()`          | Join array into string         |
| `date()`             | Formats date/time              |

## Connecting to MySQL (MySQLi)
```php
<?php
  $conn = new mysqli("localhost", "root", "", "database");

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  echo "Connected successfully!";
?>
```

## Common Mistakes to Avoid
- Forgetting to close PHP tags: `?>`
- Using `echo` without `;`
- Mixing up `GET` and `POST`
- Forgetting to sanitize inputs (`htmlspecialchars()`)
