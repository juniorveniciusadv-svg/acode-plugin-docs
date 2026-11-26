# Keyboard API

The Keyboard API provides functionality for handling keyboard events and managing keyboard state in Acode plugins. It allows you to detect keyboard visibility, respond to keyboard events, and manage keyboard-related behaviors.

## Usage

```js
const keyboard = acode.require('keyboard');
```

## Events

The keyboard module emits the following events that you can listen to:

- `key` - Triggered when a keyboard key is pressed
- `keyboardShow` - Triggered when the soft keyboard becomes visible
- `keyboardHide` - Triggered when the soft keyboard is hidden
- `keyboardShowStart` - Triggered when the soft keyboard starts to show
- `keyboardHideStart` - Triggered when the soft keyboard starts to hide

## Methods

### on(eventName, callback)

Add an event listener for keyboard events.

```js
keyboard.on('keyboardShow', () => {
		// Handle keyboard show
		console.log('Keyboard is now visible');
});

keyboard.on('key', (event) => {
		// Handle key press
		if (event.key === 'Enter' && event.ctrlKey) {
				console.log('Ctrl+Enter pressed');
		}
});
```

Parameters:
- `eventName` (string) - Name of the event to listen for ('key', 'keyboardShow', 'keyboardHide', etc.)
- `callback` (Function) - Function to execute when the event occurs

### off(eventName, callback)

Remove an event listener.

```js
const keyboardCallback = () => {
		console.log('Keyboard shown');
};

// Add listener
keyboard.on('keyboardShow', keyboardCallback);

// Remove listener
keyboard.off('keyboardShow', keyboardCallback);
```

Parameters:
- `eventName` (string) - Name of the event to remove listener from
- `callback` (Function) - The callback function to remove

### escKey State

The keyboard API includes an `escKey` state that tracks whether the Escape key is currently pressed:

```js
// Check if Escape key is pressed
if (keyboard.escKey) {
		console.log('Escape key is pressed');
}
```

## Example Plugin

Here's a complete example of using the keyboard API in an Acode plugin. Listeners are registered inside `init` and removed in `destroy`, so they do not pile up when the plugin is disabled or reloaded (see [Understanding Plugins](../getting-started/understanding-plugin.md)).

```js
import plugin from "../plugin.json";

class KeyboardPlugin {
	keyboard = null;

	onShow = () => {
		console.log("Soft keyboard shown");
	};

	onHide = () => {
		console.log("Soft keyboard hidden");
	};

	onKey = (e) => {
		// Compare in lowercase so Shift/Caps Lock don't break the match, and
		// accept Ctrl (Windows/Linux) or Command (macOS).
		if (e.key?.toLowerCase() === "s" && (e.ctrlKey || e.metaKey)) {
			console.log("Save shortcut pressed");
		}
	};

	async init() {
		this.keyboard = acode.require("keyboard");
		this.keyboard.on("keyboardShow", this.onShow);
		this.keyboard.on("keyboardHide", this.onHide);
		this.keyboard.on("key", this.onKey);
	}

	async destroy() {
		if (!this.keyboard) return;
		this.keyboard.off("keyboardShow", this.onShow);
		this.keyboard.off("keyboardHide", this.onHide);
		this.keyboard.off("key", this.onKey);
		this.keyboard = null;
	}
}

if (window.acode) {
	const acodePlugin = new KeyboardPlugin();

	acode.setPluginInit(plugin.id, async () => {
		await acodePlugin.init();
	});

	acode.setPluginUnmount(plugin.id, () => {
		acodePlugin.destroy();
	});
}
```

This example demonstrates listening for keyboard visibility changes and reacting to a keyboard shortcut. Keep the `key` handler light: it runs for key presses, not only for the shortcut you care about. The handler only logs; call the editor command you need (for example from the [Commands](./commands.md) API) instead of showing an alert.
