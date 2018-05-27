from django.test import TestCase
from lists.forms import EMPTY_ITEM_ERROR, ItemForm


class ItemFormTest(TestCase):

    def test_forms_renders_item_text(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item', form.as_p())
        self.assertIn('class="form-control input-lg', form.as_p())

    def test_forms_validation_for_blank_items(self):
        form = ItemForm(data={'test': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )
