#ifndef __DECORATOR__
#define __DECORATOR__

#include "asciiart.h"

class Decorator : public AsciiArt {
protected:
  AsciiArt *component;

public:
  Decorator(AsciiArt *component);
  virtual ~Decorator();
};

#endif
