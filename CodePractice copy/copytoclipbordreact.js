import React from 'react';

const CopyToClipboard = () => {
  const textToCopy = 'Hello, world!';

  const handleCopyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(textToCopy);
      alert('Text copied to clipboard!');
    } catch (error) {
      console.error('Failed to copy text: ', error);
    }
  };

  return (
    <div>
      <button onClick={handleCopyToClipboard}>Copy Text</button>
    </div>
  );
};

export default CopyToClipboard;


import React from 'react';

const ScreenResolution = () => {
  const screenWidth = window.screen.width;
  const screenHeight = window.screen.height;

  return (
    <div>
      <p>Screen Width: {screenWidth}px</p>
      <p>Screen Height: {screenHeight}px</p>
    </div>
  );
};

export default ScreenResolution;
