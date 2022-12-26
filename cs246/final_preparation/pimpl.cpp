#include <algorithm>
#include <vector>

class WidgetImpl;

class Widget {
public:
	Widget();
	~Widget();
	void sortData();

private:
	WidgetImpl* pImpl;
};

class WidgetImpl {
public:
	WidgetImpl(Widget* widget);
	~WidgetImpl();

	void sortData();

private:
	Widget*          widget;
	std::vector<int> m_data;
};

Widget::Widget() {
	pImpl = new WidgetImpl(this);
}

Widget::~Widget() {
	delete pImpl;
}

void Widget::sortData() {
	pImpl->sortData();
}

WidgetImpl::WidgetImpl(Widget* widget) : widget(widget) {
	// Initialize m_data with some values
}

WidgetImpl::~WidgetImpl() {}

void WidgetImpl::sortData() {
	std::sort(m_data.begin(), m_data.end());
}

int main() {
	Widget w;
	w.sortData();
	return 0;
}
