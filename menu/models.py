from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=155, unique=True, verbose_name=_("نام"))
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True, verbose_name=_("تصویر"))
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name=_("گروه")
    )
    class Meta:
        verbose_name = _("کتگوری")
        verbose_name_plural = _("گتگوری ها")

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items',verbose_name = _("کتگوری"))
    title = models.CharField(max_length=155, verbose_name = _("نام غذا"))
    description = models.TextField(blank=True, verbose_name = _("توضیحات"))
    price = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True, verbose_name = _("قیمت"))
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True, verbose_name = _("تصویر"))
    is_available = models.BooleanField(default=True, verbose_name = _("موجود"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = _("تاریخ ایجاد"))

    class Meta:
        ordering = ['category', 'title']
        verbose_name = _("نام آیتم")
        verbose_name_plural = _("آیتم ها")
    def __str__(self):
        return self.title