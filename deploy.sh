set -e

# Compile kernel
make

# Install modules
make modules_install

# Copy kernel to its location
cp /root/repos/mptcp/arch/x86_64/boot/bzImage /boot/vmlinuz-linux091

# Create initramfs
mkinitcpio -p linux091

# New bootloader
grub-mkconfig -o /boot/grub/grub.cfg
