# createKeyboardEvent

The `createKeyboardEvent` API allows you to programmatically create and dispatch keyboard events in Acode. This is useful for simulating keyboard interactions and testing keyboard-driven features.

## Import

```js
const createKeyboardEvent = acode.require('createKeyboardEvent');
```

## Usage

```js
// Create a keyboard event
const event = createKeyboardEvent('keydown', {
		key: 'Enter',
		ctrlKey: true,
		bubbles: true
});

// Dispatch the event on the element that should receive it
(document.activeElement || document).dispatchEvent(event);
```

::: warning Synthetic events
Events created from code are not trusted (`event.isTrusted` is `false`). They only reach the listeners that handle them; the browser does not perform the default action, such as inserting a character or a line break.

To reach a listener attached to an element, dispatch the event on that element (for example `document.activeElement`) and set `bubbles: true`, instead of dispatching only on `document`. A full key press is a `keydown` followed by a `keyup`.
:::

## API Reference

### createKeyboardEvent(type, options)

Creates a new keyboard event with the specified type and options.

#### Parameters

- `type` (*string*) - The type of keyboard event to create. Can be either:
	- `'keydown'` - Key pressed down
	- `'keyup'` - Key released

- `options` (*object*) - Configuration options for the keyboard event:
	- `key` (*string*) - The key value (e.g. 'Enter', 'a', 'ArrowLeft')
	- `keyCode` (*number*) - The key code (optional if key is specified)
	- `which` (*number*) - The which code (optional if key is specified)
	- `ctrlKey` (*boolean*) - Whether Ctrl key is pressed (on macOS the shortcut modifier is usually Command, so use `metaKey`)
	- `shiftKey` (*boolean*) - Whether Shift key is pressed
	- `altKey` (*boolean*) - Whether Alt key is pressed
	- `metaKey` (*boolean*) - Whether Meta/Command key is pressed
	- `bubbles` (*boolean*) - Whether event bubbles up through DOM
	- `cancelable` (*boolean*) - Whether event can be canceled

#### Returns

Returns a KeyboardEvent object that can be dispatched.

## Examples

### Basic Usage

```js
// Create Enter key press
const enterPress = createKeyboardEvent('keydown', {
		key: 'Enter'
});

// Create Ctrl+S combination (use `metaKey: true` for Command+S on macOS)
const ctrlS = createKeyboardEvent('keydown', {
		key: 's',
		ctrlKey: true
});

// Create arrow key event
const arrowLeft = createKeyboardEvent('keydown', {
		key: 'ArrowLeft'
});
```

### Simulating Shortcuts

```js
// Build a Ctrl+Alt+Delete event (it only reaches listeners; it does not trigger any operating system action)
const ctrlAltDel = createKeyboardEvent('keydown', {
		key: 'Delete',
		ctrlKey: true,
		altKey: true
});

// Simulate Shift+Enter
const shiftEnter = createKeyboardEvent('keydown', {
		key: 'Enter',
		shiftKey: true
});
```

### Working with Key Codes

```js
// Using key codes instead of key names
const backspace = createKeyboardEvent('keydown', {
		keyCode: 8 // Backspace key code
});

// Both key and keyCode can be used
const enter = createKeyboardEvent('keydown', {
		key: 'Enter',
		keyCode: 13
});
```

## Supported Keys

Common supported keys include:

- Arrow keys: `ArrowLeft`, `ArrowRight`, `ArrowUp`, `ArrowDown`
- Special keys: `Enter`, `Tab`, `Backspace`, `Delete`, `Escape`, `Space`
- Modifier keys: `Shift`, `Control`, `Alt`, `Meta`
- Function keys: `F1`-`F12`
- Printable characters: `a-z`, `A-Z`, `0-9`, symbols
