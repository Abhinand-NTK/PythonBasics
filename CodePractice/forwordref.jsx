import React, { forwardRef, useRef } from 'react';

// ChildComponent using forwardRef
const ChildComponent = forwardRef((props, ref) => {
  return (
    <input type="text" ref={ref} />
  );
});

// ParentComponent
const ParentComponent = () => {
  const inputRef = useRef(null);

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <ChildComponent ref={inputRef} />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
};

export default ParentComponent;
