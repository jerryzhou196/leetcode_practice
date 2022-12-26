#include "decorator.h"
#include "asciiart.h"

Decorator::Decorator(AsciiArt *component) : component{component} {}

Decorator::~Decorator() { delete component; }
